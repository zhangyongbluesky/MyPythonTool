import shutil;
import os;

def TCLS_Copy_ClientSwf():
	src = "E:\\Work\\QSGame_Depot\\code\\ToolSource\\TCLS\\bin-release\\QSClient.swf"
	des = "E:\\Work\\QSGame_Depot\\output\\TCLS\\ui\\QSClient.swf"
	shutil.copyfile(src, des)


def OpenDirDept(str):
	os.system("explorer.exe %s" % str);


def OpenTcls():
	OpenDirDept(r"E:\Work\QSGame_Depot\output\TCLS");


if __name__ == '__main__':
	OpenTcls();
	#os.system("p4.exe");
