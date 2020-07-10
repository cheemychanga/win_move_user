#!powershell

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


