package com.prekiraUml.plantumlplugin;

public class DtoMap {
	
	public String className = "";
	public String fullClassName = "";
	public Annotation annotations;
	public Property[] properties;
	
	
	public String toString() {
		return className;
	}
	
	
	public class Annotation {
		public String Audited;
		public String isDto;
		
		public String notRequired;
		public String isOptional;
		

		public String isMap;
		public String mapKeyType;
	}
	
	public class Property {
		public String name;
		public String dtoClassName;
		public String type;
		public Annotation[] annotations;
		public DtoEnum dtoEnums;
		
	}
	
	public class DtoEnum {
		public EnumValue value;
	}
	
	public class EnumValue {
		public String name;
		public Value[] values;
	}
	
	public class Value {
		public String name;
	}
	
}
