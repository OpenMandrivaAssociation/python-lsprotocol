Name:		python-lsprotocol
Version:	2025.0.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/l/lsprotocol/lsprotocol-%{version}.tar.gz
Summary:	Python types for Language Server Protocol.
URL:		https://pypi.org/project/lsprotocol/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Python types for Language Server Protocol.

%files
%{py_sitedir}/lsprotocol
%{py_sitedir}/lsprotocol-*.*-info
