/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.herry.test.dynamicproxy.dp2;

public class TestProxy {

	public static void main(String[] args) {
		BookFacadeProxy proxy = new BookFacadeProxy();
		BookFacade bookProxy = (BookFacade) proxy.bind(new BookFacadeImpl());
		bookProxy.addBook();
                bookProxy.removeBook();
	}

}
