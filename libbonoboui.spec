Summary:	Bonobo user interface components
Summary(pl):	Komponenty interfejsu u¿ytkownika do Bonobo
Name:		libbonoboui
Version:	1.117.0
Release:	3
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/libbonoboui/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 1.1.10
BuildRequires:	ORBit2-devel >= 2.3.110
BuildRequires:	bonobo-activation-devel >= 0.9.9
BuildRequires:	gtk+2-devel >= 2.0.2
BuildRequires:	intltool >= 0.21
BuildRequires:	libart_lgpl-devel >= 2.3.8
BuildRequires:	libbonobo-devel >= 1.117.0
BuildRequires:	libglade2-devel >= 1.99.12
BuildRequires:	libgnome-devel >= 1.117.0
BuildRequires:	libgnomecanvas-devel >= 1.117.0
BuildRequires:	libxml2-devel >= 2.4.21
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
Requires:	GConf2-devel >= 1.1.10
Requires:	libart_lgpl-devel >= 2.3.8
Requires:	libbonobo-devel >= 1.117.0
Requires:	libglade2-devel >= 1.99.12
Requires:	libgnome-devel >= 1.117.0
Requires:	libgnomecanvas-devel >= 1.117.0
Requires:	libxml2-devel >= 2.4.21
Requires:	openssl-devel

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
rm -d missing
libtoolize --copy --force
aclocal
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc=no

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

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
%attr(755,root,root) %{_libdir}/libglade/2.0/*.??
%{_libdir}/bonobo/servers/*
%{_libdir}/bonobo-2.0/samples/*
%{_datadir}/gnome-2.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/libbonoboui-2.0

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
