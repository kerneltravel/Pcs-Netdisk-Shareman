# -*- mode: python -*-
a = Analysis(['main.py'],
             pathex=['D:\\tmp\\baidu\\pcs_auto_downloader\\pyqt_APPframework_mvc\\src'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\main', 'main.exe'),
          debug=False,
          strip=None,
          upx=True,
          console=False )
coll = COLLECT(exe,
              [('translations/cn.qm', 'translations/cn.qm', 'DATA')],
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name=os.path.join('dist', 'main'))
