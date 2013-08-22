/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.herry.test.dynamicproxy.dp3;
public class TestCglib {
	
	public static void main(String[] args) {
		BookFacadeCglib cglib=new BookFacadeCglib();
		BookFacadeImpl bookCglib=(BookFacadeImpl)cglib.getInstance(new BookFacadeImpl());
		bookCglib.addBook();
                bookCglib.removeBook();
	}
}

