#!powershell


## Copyright 2020 Colton Hughes <colton.hughes@firemon.com>

## Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
## The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


#AnsibleRequires -CSharpUtil Ansible.Basic

$spec = @{
    options = @{
        name = @{ type = "str"; required = $true}
        path = @{ type = "str"; required = $true}
    }
}

$module = [Ansible.Basic.AnsibleModule]::Create($args, $spec)

$name = $module.Params.name
$path = $module.Params.path

## Find users Distinguished Name
$initPath = (Get-ADUser -Identity $name).DistinguishedName

## Filter path to only return path and not return user path
$before_value = ($initPath.Split(",", 2)[1])

## Provide details in the return value
$module.Result.old_path = $before_value


if ($before_value -ne $path)
{
    
    ## Move user to given path
    Move-ADObject -Identity (Get-ADUser -Identity $name) -TargetPath $path
    ## Mark as changed
    $module.Result.changed = $true
    ## Provide details in the return value
    $module.Result.new_path = $path
}
## if paths are equal do nothing
elseif ($before_value -eq $path){
    ## Mark as no change
    $module.Result.Changed = $false
}
else {
    ## Fail Module
    $module.FailJson("Could not move object")
     ## Mark as no change
    $module.Result.changed = $false
}
$module.ExitJson()


