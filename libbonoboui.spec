#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Bonobo user interface components
Summary(pl.UTF-8):	Komponenty interfejsu użytkownika do Bonobo
Name:		libbonoboui
Version:	2.24.5
Release:	6
License:	LGPL v2+
Group:		X11/Libraries
Source0:	https://download.gnome.org/sources/libbonoboui/2.24/%{name}-%{version}.tar.bz2
# Source0-md5:	853be8e28aaa4ce48ba60be7d9046bf4
Patch0:		%{name}-includes.patch
Patch1:		types.patch
URL:		https://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gtk+2-devel >= 2:2.12.8
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libbonobo-devel >= 2.24.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomecanvas-devel >= 2.20.0
BuildRequires:	libgnome-devel >= 2.24.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	pango-devel
BuildRequires:	pangox-compat-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	xorg-lib-libX11-devel
BuildConflicts:	gdk-pixbuf-devel < 0.12
Requires:	GConf2-libs >= 2.24.0
Requires:	glib2 >= 1:2.6.0
Requires:	gtk+2 >= 2:2.12.8
Requires:	libbonobo >= 2.24.0
Requires:	libgnome-libs >= 2.24.0
Requires:	libgnomecanvas >= 2.20.0
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
Requires:	GConf2-devel >= 2.24.0
Requires:	glib2-devel >= 1:2.6.0
Requires:	gtk+2-devel >= 2:2.12.8
Requires:	libbonobo-devel >= 2.24.0
Requires:	libglade2-devel >= 1:2.6.2
Requires:	libgnome-devel >= 2.24.0
Requires:	libgnomecanvas-devel >= 2.20.0
Requires:	libxml2-devel >= 1:2.6.31

%description devel
This package contains header files used to compile programs that use
libbonoboui.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do kompilacji programów
używających libbonoboui.

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
BuildArch:	noarch

%description apidocs
libbonoboui API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libbonoboui.

%package examples
Summary:	libbonoboui - example programs
Summary(pl.UTF-8):	libbonoboui - przykładowe programy
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
BuildArch:	noarch

%description examples
libbonoboui - example programs.

%description examples -l pl.UTF-8
libbonoboui - przykładowe programy.

%package -n gnome-bonobo-browser
Summary:	Bonobo component viewer
Summary(pl.UTF-8):	Przeglądarka komponentów bonobo
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description -n gnome-bonobo-browser
Shows available Bonobo components.

%description -n gnome-bonobo-browser -l pl.UTF-8
Wyświetla dostępne komponenty bonobo.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__gtkdocize}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PATH_TO_XRDB=/usr/bin/xrdb \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C samples clean
find samples/ -type d -name ".deps" -exec rm -rf {} \; || :
find samples/ -type f -name "Makefile*" -exec rm -f {} \;
cp -r samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# no static modules and *.la for glade modules
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libglade/2.0/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libglade/2.0/*.a
%endif
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/{sr@ije,sr@ijekavian}

%find_lang %{name}-2.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-2.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/test-moniker
%attr(755,root,root) %{_libdir}/libbonoboui-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbonoboui-2.so.0
%attr(755,root,root) %{_libdir}/libglade/2.0/libbonobo.so
%{_libdir}/bonobo/servers/Bonobo_Sample_Controls.server
%{_libdir}/bonobo/servers/CanvDemo.server
%attr(755,root,root) %{_libdir}/bonobo-2.0/samples/bonobo-sample-controls-2
%dir %{_datadir}/gnome-2.0
%dir %{_datadir}/gnome-2.0/ui
%{_datadir}/gnome-2.0/ui/Bonobo_Sample_Container-ui.xml
%{_datadir}/gnome-2.0/ui/Bonobo_Sample_Hello.xml

%files devel
%defattr(644,root,root,755)
%doc doc/*.xml doc/*.txt doc/*.html doc/*.dtd
%attr(755,root,root) %{_libdir}/libbonoboui-2.so
%{_pkgconfigdir}/libbonoboui-2.0.pc
%{_includedir}/libbonoboui-2.0

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libbonoboui-2.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libbonoboui

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files -n gnome-bonobo-browser
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bonobo-browser
%{_datadir}/gnome-2.0/ui/bonobo-browser.xml
%{_desktopdir}/bonobo-browser.desktop
