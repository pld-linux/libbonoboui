%define libxml2_version 2.4.12
%define orbit2_version 2.3.103
%define bonobo_activation_version 0.9.3.91
%define libbonobo_version 1.110.0
%define libgnomecanvas_version 1.110.0
%define libgnome_version 1.110.0
%define libart_lgpl_version 2.3.8
%define gtk2_version 1.3.13
%define libglade2_version 1.99.5.90

Summary:	Bonobo user interface components
Name:		libbonoboui
Version:	1.110.0
Release:	4
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/Библиотеки
Group(uk):	X11/Б╕бл╕отеки
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/libbonoboui/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
Requires:	libxml2 >= %{libxml2_version}
Requires:	ORBit2 >= %{orbit2_version}
Requires:	bonobo-activation >= %{bonobo_activation_version}
Requires:	libbonobo >= %{libbonobo_version}
Requires:	libgnomecanvas >= %{libgnomecanvas_version}
Requires:	libgnome >= %{libgnome_version}
Requires:	libart_lgpl >= %{libart_lgpl_version}
Requires:	gtk2 >= %{gtk2_version}
Requires:	libglade2 >= %{libglade2_version}
BuildPreReq:	libxml2-devel >= %{libxml2_version}
BuildPreReq:	ORBit2-devel >= %{orbit2_version}
BuildPreReq:	bonobo-activation-devel >= %{bonobo_activation_version}
BuildPreReq:	libbonobo-devel >= %{libbonobo_version}
BuildPreReq:	libgnomecanvas-devel >= %{libgnomecanvas_version}
BuildPreReq:	libgnome-devel >= %{libgnome_version}
BuildPreReq:	libart_lgpl-devel >= %{libart_lgpl_version}
BuildPreReq:	gtk2-devel >= %{gtk2_version}
BuildPreReq:	libglade2-devel >= %{libglade2_version}
BuildPreReq:	intltool >= 0.14-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Bonobo is a component system based on CORBA, used by the GNOME
desktop. libbonoboui contains the user interface related components
that come with Bonobo.

%package devel
Summary:	Libraries and headers for libbonoboui
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Разработка/Библиотеки
Group(uk):	X11/Розробка/Б╕бл╕отеки
Requires:	%name = %{version}
Requires:	libxml2-devel >= %{libxml2_version}
Requires:	ORBit2-devel >= %{orbit2_version}
Requires:	bonobo-activation-devel >= %{bonobo_activation_version}
Requires:	libbonobo-devel >= %{libbonobo_version}
Requires:	libgnomecanvas-devel >= %{libgnomecanvas_version}
Requires:	libgnome-devel >= %{libgnome_version}
Requires:	libart_lgpl-devel >= %{libart_lgpl_version}
Requires:	gtk2-devel >= %{gtk2_version}
Requires:	libglade2-devel >= %{libglade2_version}
Conflicts:	bonobo-devel < 1.0.8

%description devel
Bonobo is a component system based on CORBA, used by the GNOME
desktop. libbonoboui contains GUI components that come with Bonobo.

This package contains header files used to compile programs that use
libbonoboui.

%prep
%setup -q

%build
# intltool 0.13 wants NDBM_File, which we don't include 
intltoolize --force --copy
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)

%doc AUTHORS ChangeLog NEWS README

%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_libdir}/libglade/2.0/*
%{_libdir}/bonobo
%{_datadir}/gnome-2.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_libdir}/lib*.a
%{_libdir}/pkgconfig/*
%{_includedir}/*
