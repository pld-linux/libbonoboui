Summary:	Bonobo user interface components
Summary(pl):	Komponenty interfejsu u¿ytkownika do Bonobo
Name:		libbonoboui
Version:	2.4.2
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.4/%{name}-%{version}.tar.bz2
# Source0-md5:	783ecfccf1ade0d40c273cd5eee48349
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.3.3
BuildRequires:	ORBit2-devel >= 2.7.6
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common
BuildRequires:	gtk+2-devel >= 2.2.2
BuildRequires:	intltool >= 0.22
BuildRequires:	libart_lgpl-devel >= 2.3.14
BuildRequires:	libbonobo-devel >= 2.4.0
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnome-devel >= 2.3.3
BuildRequires:	libgnomecanvas-devel >= 2.3.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.5.7
BuildRequires:	openssl-devel >= 0.9.7c
BuildRequires:	rpm-build >= 4.1-10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bonobo is a component system based on CORBA, used by the GNOME
desktop. libbonoboui contains the user interface related components
that come with Bonobo.

%description -l pl
Bonobo jest systemem komponentów bazuj±cym na CORB-ie, u¿ywanym przez
¶rodowisko GNOME. libbonoboui zawiera komponenty zwi±zane z
interfejsem u¿ytkownika, które przychodz± z Bonobo.

%package devel
Summary:	Headers for libbonoboui
Summary(pl):	Pliki nag³ówkowe libbonoboui
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	GConf2-devel >= 1.2.1
Requires:	libart_lgpl-devel >= 2.3.10
Requires:	libbonobo-devel >= 2.0.0
Requires:	libglade2-devel >= 2.0.0
Requires:	libgnome-devel >= 2.0.2
Requires:	libgnomecanvas-devel >= 2.0.2
Requires:	libxml2-devel >= 2.4.23
Requires:	openssl-devel >= 0.9.7c

%description devel
Bonobo is a component system based on CORBA, used by the GNOME
desktop. libbonoboui contains GUI components that come with Bonobo.

This package contains header files used to compile programs that use
libbonoboui.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe potrzebne do kompilacji programów
u¿ywaj±cych libbonoboui.

%package static
Summary:	Static libbonoboui library
Summary(pl):	Statyczna biblioteka libbonoboui
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains static version of libbonoboui.

%description static -l pl
Ten pakiet zawiera statyczn± wersjê biblioteki libbonoboui.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoconf}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no static modules
rm -f $RPM_BUILD_ROOT%{_libdir}/libglade/2.0/*.a

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/libglade/2.0/*.so
%{_libdir}/libglade/2.0/*.la
%{_libdir}/bonobo/servers/*
%{_libdir}/bonobo-2.0/samples/*
%{_datadir}/gnome-2.0

%files devel
%defattr(644,root,root,755)
%doc doc/*.xml doc/*.txt doc/*.html doc/*.dtd
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/libbonoboui-2.0
%{_gtkdocdir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
