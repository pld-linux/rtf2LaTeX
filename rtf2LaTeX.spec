Summary:	RTF to LaTeX converter
Summary(pl):	Konwerter z formatu RTF na LaTeX
Name:		rtf2LaTeX
Version:	1.5
Release:	1
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(pl):	Aplikacje/Tekst
Source0:	http://www.ctan.org/tex-archive/support/rtf2latex/%{name}.%{version}.tar.gz
Patch0:		%{name}-reader.c-fix.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RTF to LaTeX converter.

%description -l pl
Konwerter plików z formatu RTF na LaTeX.

%prep
%setup -q -n %{name}
%patch

%build
cp Makefile.2LaTeX Makefile
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	RTFDIR=%{_datadir}/rtf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/rtf}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	RTFDIR=$RPM_BUILD_ROOT%{_datadir}/rtf \

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
%{_datadir}/rtf
