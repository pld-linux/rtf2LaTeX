Summary:	RTF to LaTeX converter.
Summary(pl):	Konwerter z formatu RTF na LaTeX.
Name:		rtf2LaTeX
Version:	1.5
Release:	1
Copyright:	GPL
Group:		Tools
Group(pl):	Narzêdzia
Source0:	%name.%version.tar.gz
Patch0:		%name-reader.c-fix.patch
#BuildRequires:	
#Requires:	
Buildroot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr

%description

%description -l pl


%prep
%setup -q -n %name

%patch

%build
#./configure --prefix=%{_prefix}
cp Makefile.2LaTeX Makefile
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" RTFDIR=%{_datadir}/rtf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/lib/rtf}
make prefix=$RPM_BUILD_ROOT%{_prefix} \
    BINDIR=$RPM_BUILD_ROOT%{_bindir} \
    MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
    RTFDIR=$RPM_BUILD_ROOT%{_datadir}/lib/rtf \
    install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%attr(644,root,root) %{_mandir}/man1/*.gz
%attr(644,root,root) %{_datadir}/lib/rtf/*
