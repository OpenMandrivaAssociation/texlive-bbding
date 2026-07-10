%global tl_name bbding
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.01
Release:	%{tl_revision}.1
Summary:	A symbol (dingbat) font and LaTeX macros for its use
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/bbding
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bbding.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bbding.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bbding.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A symbol font (distributed as Metafont source) that contains many of the
symbols of the Zapf dingbats set, together with an NFSS interface for
using the font. An Adobe Type 1 version of the fonts is available in the
niceframe fonts bundle.

