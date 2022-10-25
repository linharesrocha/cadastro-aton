pyinstaller --noconsole --name="Mordomo" --icon="..\favicon.ico" ..\mordomo\main.py
Copy-Item "C:\workspace\cadastro-aton\favicon.ico" -Destination C:\workspace\cadastro-aton\setup\dist\Mordomo
pause