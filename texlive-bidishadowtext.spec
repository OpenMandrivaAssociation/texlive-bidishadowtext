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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows you to typeset bidi-aware shadow text. It is a re-
implementation of the shadowtext package adding bidi support.

