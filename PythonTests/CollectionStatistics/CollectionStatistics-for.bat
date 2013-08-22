FOR /L %%i IN (0,1,1000000) DO (
	call Collection.bat
	echo '等待60秒后再次请求'
	ping 123.45.67.89 -n 1 -w 60000>nul
)