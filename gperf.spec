Summary:	A perfect hash function generator
Summary(pl):	Generator funkcji haszuj±cych
Name:		gperf
Version:	2.7.2
Release:	2
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	ftp://prep.ai.mit.edu/pub/gnu/gperf/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-no_dvi_html.patch
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gperf is a perfect hash function generator written in C++. Simply
stated, a perfect hash function is a hash function and a data
structure that allows recognition of a key word in a set of words
using exactly one probe into the data structure.

%description -l pl
Gperf jest napisanym w C+++ generatorem doskona³ych funkcji
haszujacych. Doskona³a funkcja haszuj±ca to funkcja haszuj±ca oraz
struktura danych, pozwalaj±ca rozpoznac s³owo kluczowe w zbiorze s³ów
wykorzystuj±c dok³adnie jedn± próbê.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
CXXFLAGS="%{rpmcflags} %{!?debug:-fno-rtti -fno-exceptions -fno-implicit-templates}"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%post
%fix_info_dir

%postun
%fix_info_dir

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gperf
%{_mandir}/man1/gperf.1*
%{_infodir}/gperf.info*
