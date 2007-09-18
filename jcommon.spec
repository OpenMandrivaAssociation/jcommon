Name:		jcommon
Summary:	A collection of useful classes in Java
Version:	1.0.9
Release:	%mkrel 1
Source:		http://prdownloads.sourceforge.net/jfreechart/jcommon-%{version}.tar.gz
URL:		http://www.jfree.org/jcommon/
Group:		Development/Java
License:	LGPLv2+
BuildArch:	noarch
BuildRequires:	java-devel >= 1.7.0
BuildRequires:	ant jpackage-utils
BuildRequires:	junit
Requires:	java junit
%description
JCommon is a collection of useful classes used by JFreeChart, JFreeReport
and other projects.

The library contains the common classes, which provide some global
utility functionality for both GUI and non-GUI applications. Inside the
library you'll find:
	* configuration and dependency management code
	* a general logging framework
	* text utilities
	* user interface classes for displaying information about
	  applications
	* custom layout managers
	* a date chooser panel
	* serialization utilities
	* XML parser support classes

%package -n %{name}-javadoc
Group:		Development/Java
Summary:	Javadoc for %name
%description -n %{name}-javadoc
Javadoc for %name

%prep
%setup -q 
%{__find} . -name '*.jar' -or -name '*.class' -exec %{__rm} -f {} \;

%build
cd ant
export CLASSPATH=$(/usr/bin/build-classpath junit)
JAVA_HOME=/usr/lib/jvm/java \
	/usr/bin/ant compile compile-xml compile-junit-tests javadoc

%install
%{__rm} -Rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_javadir}
%{__ln_s} %{name}-%{version}.jar %{name}.jar
%{__ln_s} %{name}-xml-%{version}.jar %{name}-xml.jar
%{__cp} -p %{name}-%{version}.jar %{name}.jar %{buildroot}%{_javadir}
%{__cp} -p %{name}-xml-%{version}.jar %{name}-xml.jar %{buildroot}%{_javadir}

%files
%doc licence-LGPL.txt README.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-xml-%{version}.jar
%{_javadir}/%{name}-xml.jar

%files -n %{name}-javadoc
%doc javadoc

