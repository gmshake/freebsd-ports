# Created by: chinsan <chinsan@mail2000.com.tw>

PORTNAME=	phpmyfaq
PORTVERSION=	3.0.8
CATEGORIES=	www
MASTER_SITES=	https://download.phpmyfaq.de/files/

MAINTAINER=	flo@FreeBSD.org
COMMENT=	Multilingual, completely database-driven FAQ-system

LICENSE=	MPL20

WRKSRC=		${WRKDIR}/${PORTNAME}

USES=		cpe php:web
USE_PHP=	filter json mysqli pcre pdf session xml xmlrpc xmlwriter zlib
IGNORE_WITH_PHP=	80 81
FAQ_DIR=	attachments data images inc pdf xml
NO_BUILD=	YES
NO_ARCH=	YES

do-install:
	@${MKDIR} ${STAGEDIR}${WWWDIR}
	@cd ${WRKSRC} && ${COPYTREE_SHARE} \* ${STAGEDIR}${WWWDIR}
.for i in ${FAQ_DIR}
	@${MKDIR} ${STAGEDIR}${WWWDIR}/${i}
.endfor

.include <bsd.port.mk>
