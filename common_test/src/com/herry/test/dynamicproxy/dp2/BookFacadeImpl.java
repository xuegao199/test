/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.herry.test.dynamicproxy.dp2;
public class BookFacadeImpl implements BookFacade {

	@Override
	public void addBook() {
		System.out.println("增加图书方法。。。");
	}

        @Override
        public void removeBook() {
            System.out.println("删除图书方法。。。");
        }

}




