FOR /L %%i IN (0,1,1000000) DO (
	call Collection.bat
	echo '�ȴ�60����ٴ�����'
	ping 123.45.67.89 -n 1 -w 60000>nul
)