#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Bonobo user interface components
Summary(pl.UTF-8):	Komponenty interfejsu użytkownika do Bonobo
Name:		libbonoboui
Version:	2.17.94
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libbonoboui/2.17/%{name}-%{version}.tar.bz2
# Source0-md5:	e82fc73b95f2f3a9a8aff7e349f17a3a
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.16.1
BuildRequires:	ORBit2-devel >= 1:2.14.7
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gtk+2-devel >= 2:2.10.9
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libbonobo-devel >= 2.17.92
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomecanvas-devel >= 2.14.0
BuildRequires:	libgnome-devel >= 2.17.92
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	GConf2 >= 2.16.1
Requires:	libbonobo >= 2.17.92
Requires:	libgnome >= 2.17.92
Requires:	libgnomecanvas >= 2.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bonobo is a component system based on CORBA, used by the GNOME
desktop. libbonoboui contains the user interface related components
that come with Bonobo.

%description -l pl.UTF-8
Bonobo jest systemem komponentów bazującym na CORB-ie, używanym przez
środowisko GNOME. libbonoboui zawiera komponenty związane z
interfejsem użytkownika, które przychodzą z Bonobo.

%package devel
Summary:	Headers for libbonoboui
Summary(pl.UTF-8):	Pliki nagłówkowe libbonoboui
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	GConf2-devel >= 2.16.1
Requires:	ORBit2-devel >= 2.14.7
Requires:	libbonobo-devel >= 2.17.92
Requires:	libglade2-devel >= 1:2.6.0
Requires:	libgnome-devel >= 2.17.92
Requires:	libgnomecanvas-devel >= 2.14.0
Requires:	libxml2-devel >= 1:2.6.27

%description devel
Bonobo is a component system based on CORBA, used by the GNOME
desktop. libbonoboui contains GUI components that come with Bonobo.

This package contains header files used to compile programs that use
libbonoboui.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do kompilacji programów
używających libbonoboui.

%package -n gnome-bonobo-browser
Summary:	Bonobo component viewer
Summary(pl.UTF-8):	Przeglądarka komponentów bonobo
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description -n gnome-bonobo-browser
Shows available Bonobo components.

%description -n gnome-bonobo-browser -l pl.UTF-8
Wyświetla dostępne komponenty bonobo.

%package static
Summary:	Static libbonoboui library
Summary(pl.UTF-8):	Statyczna biblioteka libbonoboui
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static version of libbonoboui.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną wersję biblioteki libbonoboui.

%package apidocs
Summary:	libbonoboui API documentation
Summary(pl.UTF-8):	Dokumentacja API libbonoboui
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libbonoboui API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libbonoboui.

%prep
%setup -q
%patch0 -p1

%build
%{__gtkdocize}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no static modules and *.la for glade modules
rm -f $RPM_BUILD_ROOT%{_libdir}/libglade/2.0/*.{la,a}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
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

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif

%files -n gnome-bonobo-browser
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bonobo-browser
%{_desktopdir}/*.desktop

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
