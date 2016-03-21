import shutil;
import os;

def EditDeptFileByP4(str):
	os.system("p4.exe -c rockiezhang_rockiezhang-PC0_1244 edit %s" % str);

def EditProtocolSrc(str):
	EditDeptFileByP4(str);

def EditProtocolDes(str):
	EditDeptFileByP4(str);

if __name__ == '__main__':
	#EditDeptFileByP4("E:\\Work\\QSGame_Depot\\output\\XYGameServer.fcf");

	strSrc = "-c 360831 E:\\Work\\QSGame_Depot\\cs_share\\proto\\*";
	strDesHeader = "-c 360832 E:\\Work\\QSGame_Depot\\code\\Include\\GeNetModule\\protocol\\*";
	strDesCpp = "-c 360832 E:\\Work\\QSGame_Depot\\code\\CoreSource\\GeNetModule\\xynet\\*";
	EditProtocolSrc(strSrc);
	EditProtocolDes(strDesHeader);
	EditProtocolDes(strDesCpp);