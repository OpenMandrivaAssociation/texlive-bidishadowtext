%global tl_name bidishadowtext
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Bidi-aware shadow text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/bidishadowtext
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bidishadowtext.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bidishadowtext.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows you to typeset bidi-aware shadow text. It is a re-
implementation of the shadowtext package adding bidi support.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/xelatex
%dir %{_datadir}/texmf-dist/tex/xelatex
%dir %{_datadir}/texmf-dist/doc/xelatex/bidishadowtext
%dir %{_datadir}/texmf-dist/tex/xelatex/bidishadowtext
%doc %{_datadir}/texmf-dist/doc/xelatex/bidishadowtext/bidishadowtext-demo.pdf
%doc %{_datadir}/texmf-dist/doc/xelatex/bidishadowtext/bidishadowtext-demo.tex
%doc %{_datadir}/texmf-dist/doc/xelatex/bidishadowtext/bidishadowtext-doc.pdf
%doc %{_datadir}/texmf-dist/doc/xelatex/bidishadowtext/bidishadowtext-doc.tex
%{_datadir}/texmf-dist/tex/xelatex/bidishadowtext/bidishadowtext.sty
