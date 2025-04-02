#include "..\common\common.h"


void DEBUG_LOG(char text[]) {
    if (DEBUG_MODE) {
        printf("DEBUG: %s", text);
    }
}