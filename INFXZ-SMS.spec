# -*- mode: python ; coding: utf-8 -*-
a = Analysis(['INFXZ-SMS.py'], pathex=[], hiddenimports=['requests', 'colorama'], noarchive=False)
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, a.binaries, a.datas, name='INFXZ-SMS', console=True)

