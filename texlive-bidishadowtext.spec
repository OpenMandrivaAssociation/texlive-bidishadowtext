Name:		texlive-bidishadowtext
Version:	34633
Release:	1
Summary:	Bidi-aware shadow text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bidishadowtext
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bidishadowtext.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bidishadowtext.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows you to typeset bidi-aware shadow text. It
is a re-implementation of the shadowtext package adding bidi
support.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/bidishadowtext
%doc %{_texmfdistdir}/doc/xelatex/bidishadowtext

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
