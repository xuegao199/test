/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.herry.test.dynamicproxy.dp1;

/**
 * 委托类(包含业务逻辑)
 * 
 * @author Administrator
 * 
 */
public class CountImpl implements Count {

	@Override
	public void queryCount() {
		System.out.println("查看账户方法...");

	}

	@Override
	public void updateCount() {
		System.out.println("修改账户方法...");

	}

}


