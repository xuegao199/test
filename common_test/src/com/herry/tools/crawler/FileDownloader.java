package com.herry.tools.crawler;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;

public class FileDownloader implements Runnable{
	private String httpUrl=null;
	private String path=null;
	public FileDownloader(String httpUrl){
		this.httpUrl=httpUrl;
	}
	public FileDownloader(String httpUrl,String Path){
		this(httpUrl);
		this.path=Path;
		File f=new File("Image");
		if(!f.exists()) f.mkdir();
		f=null;
		File fi=new File("Image\\"+path);
		if(!fi.exists()) fi.mkdir();
		fi=null;
	}
	
	
	@Override
	public void run() {
	    // 下载网络文件
	    int bytesum = 0;
	    int byteread = 0;
	
	    URL url = null;
		try {
			url = new URL(httpUrl);
		} catch (MalformedURLException e1) {
			e1.printStackTrace();
		}
		 FileOutputStream fs=null;
	    try {
	        URLConnection conn = url.openConnection();
	        InputStream inStream = conn.getInputStream();
	        if(path==null){
	        	fs = new FileOutputStream(getLastStringFromURL());
	        }else{
	        	fs= new FileOutputStream("Image\\"+path+"\\"+getLastStringFromURL());
	        }
	        byte[] buffer = new byte[1024];
	        while ((byteread = inStream.read(buffer)) != -1) {
	            bytesum += byteread;
	            fs.write(buffer, 0, byteread);
	        }
//	        System.out.println("下载"+httpUrl+"成功");
	    } catch (Exception e) {
	        e.printStackTrace();
	    } finally{
	    	try {
				fs.flush();
		        fs.close();
			} catch (IOException e) {
				e.printStackTrace();
			}


	    }
	}
		

/**
 * 提取URL中的文件名
 * @param url
 * @return
 */
private  String getLastStringFromURL(){
	 try{
		 String[] ss=httpUrl.split("/");
		 int i=ss.length;
		 ss[i-1]=ss[i-1].replace("?","");
		 ss[i-1]=ss[i-1].replace("v=tbs","");
		 return ss[i-1];
	 }
	 catch(Exception e){
		 System.out.println("【ERROR】"+httpUrl);
	 }
	 return null;
}

}
