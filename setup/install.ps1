# Instalar o GIT
# Instalar o Python

# Criando a Pasta workspace

Set-Location /
$Folder = 'C:\workspace'
if (Test-Path -Path $Folder) {
	"ALERT: workspace ja existe"
	"ALERT: ignorando criacao de pasta"
}
else {
	New-Item -Path 'C:\workspace' -ItemType Directory
	Write-Host " "
	"SUCESS: workspace criada"
}
Write-Host " "

# Clonando arquivos
Set-Location C:\workspace

$Folder = 'C:\workspace\cadastro-aton'
if (Test-Path -Path $Folder) {
	"ALERT: cadastro-aton ja existe"
	"ALERT: dando pull"
	git pull
}

else {
	git clone https://github.com/linharesrocha/cadastro-aton.git
	Write-Host " "
	Write-Host "SUCESS: arquivos clonados"
}


# Instalando aplicativo
Set-Location C:\workspace\cadastro-aton\
git init
git remote add origin https://github.com/linharesrocha/cadastro-aton.git
py -m ensurepip --upgrade
python -m pip install -U pip
pip install -r requirements.txt

pause