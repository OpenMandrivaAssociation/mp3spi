Name:           mp3spi
Summary:        MP3SPI - A JSPI that adds MP3 support for Java
URL:            http://www.javazoom.net/mp3spi/mp3spi.html
Group:          Development/Java
Version:        1.9.4
Release:        %mkrel 0.0.2
License:        LGPL
BuildRequires:  ant
BuildRequires:  dos2unix
BuildRequires:  jpackage-utils >= 1.5
BuildRequires:  java-rpmbuild >= 1.5
BuildRequires:  jlayer >= 1.0
BuildRequires:  tritonus-shared
BuildRequires:	update-alternatives
BuildRequires:	xml-commons-apis
BuildRequires:	xml-commons-resolver
Requires:       java >= 1.5
Requires:       jlayer >= 1.0
Requires:       tritonus-shared
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:        %{name}-%{version}.tar.bz2
Patch0:         %{name}-build.xml.diff

%description
MP3SPI is a Java Service Provider Interface that adds MP3
(MPEG 1/2/2.5 Layer 1/2/3) audio format support for Java Platform.
It supports streaming, ID3v2 frames, Equalizer, ....

It is based on JLayer and Tritonus Java libraries.

%package javadoc
Summary:     Javadoc for mp3spi
Group:       Development/Java

%description javadoc
Javadoc for mp3spi.

%prep
%setup -q -n MpegAudioSPI%{version}
%patch0
 
dos2unix     LICENSE.txt README.txt CHANGES.txt
%__chmod 644 LICENSE.txt README.txt CHANGES.txt

%build
export CLASSPATH=$(build-classpath tritonus/tritonus_share)
%ant -Dbuild.sysclasspath=first all

%install
# jars
%__install -dm 755 %{buildroot}%{_javadir}
%__install -pm 644 %{name}%{version}.jar \
	%{buildroot}%{_javadir}/%{name}-%{version}.jar

pushd %{buildroot}%{_javadir}
	for jar in *-%{version}*; do
		ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`
	done
popd

# javadoc
%__install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
%__cp -pr doc/* \
	%{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%clean
[ -d %{buildroot} -a "%{buildroot}" != "" ] && %__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_javadir}/%{name}*.jar
%doc CHANGES.txt LICENSE.txt README.txt

%files javadoc
%defattr(-,root,root)
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}
