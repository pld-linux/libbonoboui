Summary:	Bonobo user interface components
Summary(pl):	Komponenty interfejsu u¿ytkownika do Bonobo
Name:		libbonoboui
Version:	1.116.0
Release:	0.1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/libbonoboui/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel
BuildRequires:	ORBit2-devel
BuildRequires:	bonobo-activation-devel
BuildRequires:	gtk+2-devel
BuildRequires:	intltool
BuildRequires:	libart_lgpl-devel
BuildRequires:	libbonobo-devel >= 1.116
BuildRequires:	libglade2-devel
BuildRequires:	libgnome-devel >= 1.116.0
BuildRequires:	libgnomecanvas-devel >= 1.116.0
BuildRequires:	libxml2-devel
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
# intltool 0.13 wants NDBM_File, which we don't include
#ntltoolize --force --copy
%configure \
	--enable-gtk-doc=no

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/libglade/2.0/*.??
%{_libdir}/bonobo/servers/*
#%{_datadir}/gnome-2.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/libbonoboui-2.0

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
