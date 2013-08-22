/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.herry.test.dynamicproxy.dp1;

/**
 *测试Count类
 * 
 * @author Administrator
 * 
 */
public class TestCount {
	public static void main(String[] args) {
		CountImpl countImpl = new CountImpl();
		CountProxy countProxy = new CountProxy(countImpl);
		countProxy.updateCount();
		countProxy.queryCount();

	}
}

