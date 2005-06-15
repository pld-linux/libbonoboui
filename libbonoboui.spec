#
# Conditional build:
%bcond_with	xlibs	# with xlibs
%bcond_without	static	# don't build static library
#
Summary:	Bonobo user interface components
Summary(pl):	Komponenty interfejsu u¿ytkownika do Bonobo
Name:		libbonoboui
Version:	2.8.1
Release:	5
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.8/%{name}-%{version}.tar.bz2
# Source0-md5:	b23daafa8344a88696d497f20285ef55
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
%{?with_xlibs:BuildRequires:	libX11-devel}
BuildRequires:	GConf2-devel >= 2.8.0.1
BuildRequires:	ORBit2-devel >= 2.12.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	howl-devel >= 0.9.10
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gtk+2-devel >= 2:2.4.1
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	intltool >= 0.29
BuildRequires:	libbonobo-devel >= 2.8.1
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	libgnome-devel >= 2.8.0
BuildRequires:	libgnomecanvas-devel >= 2.8.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.13
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
%{?with_xlibs:BuildRequires:	sed >= 4.0}
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
Requires:	%{name} = %{version}-%{release}
Requires:	GConf2-devel >= 2.8.0.1
Requires:	libbonobo-devel >= 2.8.1
Requires:	libglade2-devel >= 1:2.4.0
Requires:	libgnome-devel >= 2.8.0
Requires:	libgnomecanvas-devel >= 2.8.0
Requires:	libxml2-devel >= 2.6.13

%description devel
Bonobo is a component system based on CORBA, used by the GNOME
desktop. libbonoboui contains GUI components that come with Bonobo.

This package contains header files used to compile programs that use
libbonoboui.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe potrzebne do kompilacji programów
u¿ywaj±cych libbonoboui.

%package -n gnome-bonobo-browser
Summary:	Bonobo component viewer
Summary(pl):	Przegl±darka komponentów bonobo
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description -n gnome-bonobo-browser
Shows available Bonobo components.

%description -n gnome-bonobo-browser -l pl
Wy¶wietla dostêpne komponenty bonobo.

%package static
Summary:	Static libbonoboui library
Summary(pl):	Statyczna biblioteka libbonoboui
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static version of libbonoboui.

%description static -l pl
Ten pakiet zawiera statyczn± wersjê biblioteki libbonoboui.

%prep
%setup -q
%patch0 -p1

%if %{with xlibs}
sed -ie \
	's/AC_PATH_XTRA/PKG_CHECK_MODULES(X, [x11], [$x_no = no])/' \
	configure.in
%endif

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	%{!?with_static:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no static modules and *.la for glade modules
rm -f $RPM_BUILD_ROOT%{_libdir}/libglade/2.0/*.{la,a}

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/test-moniker
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/libglade/2.0/*.so
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

%if %{with static}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif

%files -n gnome-bonobo-browser
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bonobo-browser
%{_desktopdir}/*.desktop
