//controller_status.h

/* Status */
#define AUTOSYN_CONTROLLER_STATUS_LED_BUILTIN   0x00000001
#define AUTOSYN_CONTROLLER_STATUS_VALVE_1       0x00000002
#define AUTOSYN_CONTROLLER_STATUS_VALVE_2       0x00000004
#define AUTOSYN_CONTROLLER_STATUS_VALVE_3       0x00000008
#define AUTOSYN_CONTROLLER_STATUS_VALVE_4       0x00000010

/* Initial status */
#define AUTOSYN_CONTROLLER_STATUS_INIT          0x00000000

/* Bitwise manipulation */
#define AUTOSYN_SET_LED_BUILTIN(status)         ((status) |= AUTOSYN_CONTROLLER_STATUS_LED_BUILTIN)
#define AUTOSYN_CLR_LED_BUILTIN(status)         ((status) &= (~AUTOSYN_CONTROLLER_STATUS_LED_BUILTIN))
#define AUTOSYN_SET_VALVE_1(status)             ((status) |= AUTOSYN_CONTROLLER_STATUS_VALVE_1)
#define AUTOSYN_CLR_VALVE_1(status)             ((status) &= (~AUTOSYN_CONTROLLER_STATUS_VALVE_1))
#define AUTOSYN_SET_VALVE_2(status)             ((status) |= AUTOSYN_CONTROLLER_STATUS_VALVE_2)
#define AUTOSYN_CLR_VALVE_2(status)             ((status) &= (~AUTOSYN_CONTROLLER_STATUS_VALVE_2))
#define AUTOSYN_SET_VALVE_3(status)             ((status) |= AUTOSYN_CONTROLLER_STATUS_VALVE_3)
#define AUTOSYN_CLR_VALVE_3(status)             ((status) &= (~AUTOSYN_CONTROLLER_STATUS_VALVE_3))