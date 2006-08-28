# TODO:
# - some no.po contain more entries than nb.po - merge them
# - finish pl :)
Summary:	List of country and language names
Summary(pl):	Lista nazw krajów i jêzyków
Name:		iso-codes
Version:	0.53
Release:	1
License:	LGPL
Group:		Applications/Text
Source0:	http://ftp.debian.org/debian/pool/main/i/iso-codes/%{name}_%{version}.orig.tar.gz
# Source0-md5:	8459445fd437e3dbe5d4b03478cd29f5
Patch0:		%{name}-pl.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	python-PyXML
Conflicts:	pkgconfig < 1:0.19
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noarchpkgconfigdir	%{_datadir}/pkgconfig

%description
This package aims to provide the list of the country and language (and
currency) names in one place, rather than repeated in many programs.

%description -l pl
Celem tego pakietu jest dostarczenie list nazw krajów i jêzyków (oraz
walut) w jednym miejscu, zamiast powtarzania ich w wielu programach.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{no,nb}/LC_MESSAGES/iso_4217.mo
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{dv,haw,kok,no,pa_IN,ps,tk,wo}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{_datadir}/iso-codes
# XXX: shared with libglade2 - make it more common?
%dir %{_datadir}/xml
%{_datadir}/xml/iso-codes
%{_noarchpkgconfigdir}/iso-codes.pc
