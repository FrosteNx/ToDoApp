# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['ToDoApp.py'],
             pathex=['C:\\Users\\Dominik\\Desktop\\sem4\\ToDoApp'],
             binaries=[],
             datas=[
                ('C:\\Users\\Dominik\\Desktop\\sem4\\ToDoApp\\to_do.ico', '.'), 
                ('C:\\Users\\Dominik\\Desktop\\sem4\\ToDoApp\\tasklist.txt', '.'),
                ('C:\\Users\\Dominik\\Desktop\\sem4\\ToDoApp\\Image\\delete1.png', '.'), 
                ('C:\\Users\\Dominik\\Desktop\\sem4\\ToDoApp\\Image\\dock.png', '.'), 
                ('C:\\Users\\Dominik\\Desktop\\sem4\\ToDoApp\\Image\\todolist.png', '.'), 
                ('C:\\Users\\Dominik\\Desktop\\sem4\\ToDoApp\\Image\\topbar.png', '.')
                ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='ToDoApp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='C:\\Users\\Dominik\\Desktop\\sem4\\ToDoApp\\to_do.ico')
