# Created by: bf <bf2006a@yahoo.com>

PORTNAME=	dieharder
PORTVERSION=	3.31.1
PORTREVISION=	9
CATEGORIES=	math
MASTER_SITES=	http://www.phy.duke.edu/~rgb/General/dieharder/ LOCAL/bf

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Random number generator testsuite

LICENSE=	GPLv2

LIB_DEPENDS=	libgsl.so:math/gsl

BROKEN_sparc64=		fails to compile
MAKE_JOBS_UNSAFE=	yes

USES=		dos2unix libtool tar:tgz
GNU_CONFIGURE=	yes
CPPFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib
USE_LDCONFIG=	yes

# Fix build with clang11
CFLAGS+=	-fcommon

check test: build
	${WRKSRC}/dieharder/dieharder -a

.include <bsd.port.mk>
