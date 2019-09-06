#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-maven-artifact
Version  : 2.0.5
Release  : 9
URL      : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.0.5/maven-artifact-2.0.5.jar
Source0  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.0.5/maven-artifact-2.0.5.jar
Source1  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.0.1/maven-artifact-2.0.1.jar
Source2  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.0.1/maven-artifact-2.0.1.pom
Source3  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.0.10/maven-artifact-2.0.10.jar
Source4  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.0.10/maven-artifact-2.0.10.pom
Source5  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.0.11/maven-artifact-2.0.11.jar
Source6  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.0.11/maven-artifact-2.0.11.pom
Source7  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.0.2/maven-artifact-2.0.2.jar
Source8  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.0.2/maven-artifact-2.0.2.pom
Source9  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.0.4/maven-artifact-2.0.4.jar
Source10  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.0.4/maven-artifact-2.0.4.pom
Source11  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.0.5/maven-artifact-2.0.5.pom
Source12  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.0.6/maven-artifact-2.0.6.jar
Source13  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.0.6/maven-artifact-2.0.6.pom
Source14  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.0.7/maven-artifact-2.0.7.jar
Source15  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.0.7/maven-artifact-2.0.7.pom
Source16  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.0.8/maven-artifact-2.0.8.jar
Source17  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.0.8/maven-artifact-2.0.8.pom
Source18  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.0.9/maven-artifact-2.0.9.jar
Source19  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.0.9/maven-artifact-2.0.9.pom
Source20  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.0/maven-artifact-2.0.pom
Source21  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.1.0/maven-artifact-2.1.0.jar
Source22  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.1.0/maven-artifact-2.1.0.pom
Source23  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.2.0/maven-artifact-2.2.0.jar
Source24  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.2.0/maven-artifact-2.2.0.pom
Source25  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.2.1/maven-artifact-2.2.1.jar
Source26  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/2.2.1/maven-artifact-2.2.1.pom
Source27  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/3.0.3/maven-artifact-3.0.3.jar
Source28  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/3.0.3/maven-artifact-3.0.3.pom
Source29  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/3.0.4/maven-artifact-3.0.4.jar
Source30  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/3.0.4/maven-artifact-3.0.4.pom
Source31  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/3.0.5/maven-artifact-3.0.5.jar
Source32  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/3.0.5/maven-artifact-3.0.5.pom
Source33  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/3.0/maven-artifact-3.0.jar
Source34  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/3.0/maven-artifact-3.0.pom
Source35  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/3.3.9/maven-artifact-3.3.9.jar
Source36  : https://repo1.maven.org/maven2/org/apache/maven/maven-artifact/3.3.9/maven-artifact-3.3.9.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-maven-artifact-data = %{version}-%{release}
Requires: mvn-maven-artifact-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
No detailed description available

%package data
Summary: data components for the mvn-maven-artifact package.
Group: Data

%description data
data components for the mvn-maven-artifact package.


%package license
Summary: license components for the mvn-maven-artifact package.
Group: Default

%description license
license components for the mvn-maven-artifact package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-maven-artifact
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-maven-artifact/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.5
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.5/maven-artifact-2.0.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.1/maven-artifact-2.0.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.1/maven-artifact-2.0.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.10
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.10/maven-artifact-2.0.10.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.10
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.10/maven-artifact-2.0.10.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.11
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.11/maven-artifact-2.0.11.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.11
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.11/maven-artifact-2.0.11.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.2
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.2/maven-artifact-2.0.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.2
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.2/maven-artifact-2.0.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.4
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.4/maven-artifact-2.0.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.4
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.4/maven-artifact-2.0.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.5
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.5/maven-artifact-2.0.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.6
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.6/maven-artifact-2.0.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.6
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.6/maven-artifact-2.0.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.7
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.7/maven-artifact-2.0.7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.7
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.7/maven-artifact-2.0.7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.8
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.8/maven-artifact-2.0.8.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.8
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.8/maven-artifact-2.0.8.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.9
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.9/maven-artifact-2.0.9.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.9
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.9/maven-artifact-2.0.9.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0/maven-artifact-2.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.1.0
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.1.0/maven-artifact-2.1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.1.0
cp %{SOURCE22} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.1.0/maven-artifact-2.1.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.2.0
cp %{SOURCE23} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.2.0/maven-artifact-2.2.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.2.0
cp %{SOURCE24} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.2.0/maven-artifact-2.2.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.2.1
cp %{SOURCE25} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.2.1/maven-artifact-2.2.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.2.1
cp %{SOURCE26} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.2.1/maven-artifact-2.2.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0.3
cp %{SOURCE27} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0.3/maven-artifact-3.0.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0.3
cp %{SOURCE28} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0.3/maven-artifact-3.0.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0.4
cp %{SOURCE29} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0.4/maven-artifact-3.0.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0.4
cp %{SOURCE30} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0.4/maven-artifact-3.0.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0.5
cp %{SOURCE31} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0.5/maven-artifact-3.0.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0.5
cp %{SOURCE32} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0.5/maven-artifact-3.0.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0
cp %{SOURCE33} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0/maven-artifact-3.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0
cp %{SOURCE34} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0/maven-artifact-3.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.3.9
cp %{SOURCE35} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.3.9/maven-artifact-3.3.9.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.3.9
cp %{SOURCE36} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.3.9/maven-artifact-3.3.9.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.1/maven-artifact-2.0.1.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.1/maven-artifact-2.0.1.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.10/maven-artifact-2.0.10.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.10/maven-artifact-2.0.10.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.11/maven-artifact-2.0.11.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.11/maven-artifact-2.0.11.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.2/maven-artifact-2.0.2.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.2/maven-artifact-2.0.2.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.4/maven-artifact-2.0.4.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.4/maven-artifact-2.0.4.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.5/maven-artifact-2.0.5.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.5/maven-artifact-2.0.5.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.6/maven-artifact-2.0.6.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.6/maven-artifact-2.0.6.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.7/maven-artifact-2.0.7.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.7/maven-artifact-2.0.7.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.8/maven-artifact-2.0.8.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.8/maven-artifact-2.0.8.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.9/maven-artifact-2.0.9.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0.9/maven-artifact-2.0.9.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.0/maven-artifact-2.0.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.1.0/maven-artifact-2.1.0.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.1.0/maven-artifact-2.1.0.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.2.0/maven-artifact-2.2.0.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.2.0/maven-artifact-2.2.0.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.2.1/maven-artifact-2.2.1.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/2.2.1/maven-artifact-2.2.1.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0.3/maven-artifact-3.0.3.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0.3/maven-artifact-3.0.3.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0.4/maven-artifact-3.0.4.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0.4/maven-artifact-3.0.4.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0.5/maven-artifact-3.0.5.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0.5/maven-artifact-3.0.5.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0/maven-artifact-3.0.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.0/maven-artifact-3.0.pom
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.3.9/maven-artifact-3.3.9.jar
/usr/share/java/.m2/repository/org/apache/maven/maven-artifact/3.3.9/maven-artifact-3.3.9.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-maven-artifact/LICENSE.txt
