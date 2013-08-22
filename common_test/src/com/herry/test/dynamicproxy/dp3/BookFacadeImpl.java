/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.herry.test.dynamicproxy.dp3;

/**
 * 这个是没有实现接口的实现类
 * 
 * @author student
 * 
 */
public class BookFacadeImpl{
	public void addBook() {
		System.out.println("增加图书的普通方法...");
	}
        
        public void removeBook() {
            System.out.println("删除图书方法。。。");
        }
}



