%define		gs_version	%(rpm -q --qf '%{VERSION}' gnome-shell)
%define		gjs_version	%(rpm -q --qf '%{VERSION}' gjs-devel)
Summary:	IBus gnome-shell extension
Summary(pl.UTF-8):	Rozszerzenie IBus dla powłoki gnome-shell
Name:		ibus-gjs
Version:	3.4.1.20120815
Release:	1
License:	LGPL v2+
Group:		Libraries
##Source0Download: http://code.google.com/p/ibus/downloads/list
#Source0:	http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
Source0:	http://fujiwara.fedorapeople.org/ibus/gnome-shell/%{name}-%{version}.tar.gz
# Source0-md5:	8acf4ac4d1a7dfb9a0af9e755a8e7dba
Patch0:		%{name}-fixes.patch
URL:		http://code.google.com/p/ibus/
BuildRequires:	gettext-devel
BuildRequires:	gjs-devel
BuildRequires:	gnome-shell
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	ibus-devel >= 1.4
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IBus gnome-shell extension.

%description -l pl.UTF-8
Rozszerzenie IBus dla powłoki gnome-shell.

%package -n ibus-gnome3
Summary:	IBus gnome-shell-extension for GNOME3
Summary(pl.UTF-8):	Rozszerzenie gnome-shell IBus dla GNOME3
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-shell

%description -n ibus-gnome3
This is a transitional package which allows users to try out new IBus
GUI for GNOME3 in development. Note that this package will be marked
as obsolete once the integration has completed in the GNOME3 upstream.

%description -n ibus-gnome3 -l pl.UTF-8
Pakiet przejściowy pozwalający użytkownikom wypróbować nowe GUI IBus
dla GNOME3 w trakcie tworzenia. Uwaga: ten pakiet zostanie oznaczony
jako przestarzały po zakończeniu integracji w GNOME3.

%prep
%setup -q
%{__rm} js/ui/status/ibus/xkbLayout.js
%patch0 -p1

%build
%configure \
	--with-gnome-shell-version="%{gs_version},3.6,3.4,3.2" \
	--with-gjs-version="%{gjs_version},1.33.3,1.32,1.31.22,1.31.20,1.31.10,1.31.6,1.31.11,1.30"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%{__rm} $RPM_BUILD_ROOT%{_localedir}/*/LC_MESSAGES/ibus-gjs.mo

%clean
rm -rf $RPM_BUILD_ROOT

%files -n ibus-gnome3
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_datadir}/gnome-shell/js/ui/status/ibus
%{_datadir}/gnome-shell/extensions/ibus-indicator@example.com
