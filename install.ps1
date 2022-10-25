# Criando a Pasta workspace

cd ..\..\
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
cd ..\..\workspace

$Folder = 'C:\workspace\cadastro-aton'
if (Test-Path -Path $Folder) {
	"ALERT: cadastro-aton ja existe"
	"ALERT: removendo pasta"
	Remove-Item 'C:\workspace\cadastro-aton' -Recurse -Force
}

git clone https://github.com/linharesrocha/cadastro-aton.git
Write-Host " "
Write-Host "SUCESS: arquivos clonados"


# Instalando aplicativo
cd ..\..\..\workspace\cadastro-aton\
py -m ensurepip --upgrade
python -m pip install -U pip
pip install -r requirements.txt
pyinstaller --noconsole --name="Mordomo" --icon="favicon.ico" .\main.py
cp favicon.ico C:\workspace\cadastro-aton\dist\Mordomo