# TODO:
# - some no.po contain more entries than nb.no - merge them
# - check for missing locale dirs and glibc support
# - finish pl :)
Summary:	List of country and language names
Summary(pl):	Lista nazw krajów i jêzyków
Name:		iso-codes
Version:	0.42
%define	bver	pre1
Release:	0.%{bver}.1
License:	LGPL
Group:		Applications/Text
Source0:	http://people.debian.org/~mckinstry/%{name}-%{version}%{bver}.tar.gz
# Source0-md5:	82e39ca14006767684d3c30d4006a153
BuildRequires:	gettext-devel
BuildRequires:	python-PyXML
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package aims to provide the list of the country and language (and
currency) names in one place, rather than repeated in many programs.

%description -l pl
Celem tego pakiet jest dostarczenie list nazw krajów i jêzyków (oraz
walut) w jednym miejscu, zamiast powtarzania ich w wielu programach.

%prep
%setup -q -n %{name}-%{version}%{bver}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{no,nb}/LC_MESSAGES/iso_4217.mo
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{_datadir}/iso-codes
# %{_datadir}/xml owned by libglade2 - make it more common or change it?
#%{_datadir}/xml/iso-codes
%{_pkgconfigdir}/iso-codes.pc
