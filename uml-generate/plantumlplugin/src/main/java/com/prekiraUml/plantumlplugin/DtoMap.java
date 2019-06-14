package com.prekiraUml.plantumlplugin;

public class DtoMap {
	
	public String className = "";
	public String fullClassName = "";
	public Annotation annotations;
	
	
	
	public String toString() {
		return className;
	}
	
	
	public class Annotation {
		public String Audited;
		public String x;
	}
	
}
