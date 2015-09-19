# C:\python27\Lib

'''
Invert Code for Arduino PWM when Digital
Channel is 'LOW' along with a few other
bits and pieces.
'''
##set_zero = 0
##
##if set_zero == 0:
##    from set_zero import *
##    set_zero = set_zero + 1
##else:
##    print "Module set_zero imported!"
class CMDmodule():
    print "Welcome to CMDmodule.  Use Wisely. "

    def __init__(self, init=0, question_two=0, a=0, b=0, debug_value=0, motor_a_prev=0, motor_b_prev=0, dir_y_prev=0):
        self.init = init
        self.question_two = question_two
        self.a = a
        self.b = b
        self.debug_value = debug_value
        self.motor_a_prev = motor_a_prev
        self.motor_b_prev = motor_b_prev
        self.dir_y_prev = dir_y_prev
        print "Valables set to Zero!"

    def invert_y_axis():
        global y
        if y < 0:               ############################
            y = abs(y)          #New Y-axes inversion code!#
        elif y > 0:             ############################
            y = y*-1

    def sendcommand(motor_a,motor_b,dir_y):
        byte1 = chr(int(motor_a))
        byte2 = chr(int(motor_b))
        byte3 = chr(int(dir_y))
        sock.send(byte1+byte2+byte3)

    def pwm_formula_test(self):
        global a
        PWM = 255
        aa = PWM*a
        aa = round(aa, 1)
        motor_a = aa

    def pwm_formula():
        global y
        global a
        global b
        PWM = 255
        a = PWM*a
        a = round(a, 1)
        b = PWM*b
        b = round(b, 1)
        motor_a = a
        motor_b = b


    def send_when_different():
        global motor_a
        global motor_b
        global motor_a_prev
        global motor_b_prev
        global dir_y
        global dir_y_prev
        if motor_a != motor_a_prev:
            sendcommand(motor_a,motor_b,dir_y)
        elif motor_b != motor_b_prev:
            sendcommand(motor_a,motor_b,dir_y)
        elif dir_y != dir_y_prev:
            sendcommand(motor_a,motor_b,dir_y)


        motor_a_prev = motor_a
        motor_b_prev = motor_b
        dir_y_prev = dir_y


    def arduino_direction():
        global y
        if y < 0:           
            y = 2           
        else:               
            y = 1
        dir_y = y


    def ardruino_direction_sPWM():
        global y
        global motor_a
        global motor_b
        if y < 0:           
            y = 2                # Backwards
            motor_a = 255 - motor_a
            motor_a = abs(motor_a)
            motor_b = 255 - motor_b
            motor_b = abs(motor_b)
        else:               
            y = 1                # Forewards
        dir_y = y


    def invert_mota():
        global motor_a
        if motor_a == 0:
            motor_a = 255
        elif motor_a == 1:
            motor_a = 254
        elif motor_a == 2:
            motor_a = 253
        elif motor_a == 3:
            motor_a = 252
        elif motor_a == 4:
            motor_a = 251
        elif motor_a == 5:
            motor_a = 250
        elif motor_a == 6:
            motor_a = 249
        elif motor_a == 7:
            motor_a = 248
        elif motor_a == 8:
            motor_a = 247
        elif motor_a == 9:
            motor_a = 246
        elif motor_a == 10:
            motor_a = 245
        elif motor_a == 11:
            motor_a = 244
        elif motor_a == 12:
            motor_a = 243
        elif motor_a == 13:
            motor_a = 242
        elif motor_a == 14:
            motor_a = 241
        elif motor_a == 15:
            motor_a = 240
        elif motor_a == 16:
            motor_a = 239
        elif motor_a == 17:
            motor_a = 238
        elif motor_a == 18:
            motor_a = 237
        elif motor_a == 19:
            motor_a = 236
        elif motor_a == 20:
            motor_a = 235
        elif motor_a == 21:
            motor_a = 234
        elif motor_a == 22:
            motor_a = 233
        elif motor_a == 23:
            motor_a = 232
        elif motor_a == 24:
            motor_a = 231
        elif motor_a == 25:
            motor_a = 230
        elif motor_a == 26:
            motor_a = 229
        elif motor_a == 27:
            motor_a = 228
        elif motor_a == 28:
            motor_a = 227
        elif motor_a == 29:
            motor_a = 226
        elif motor_a == 30:
            motor_a = 225
        elif motor_a == 31:
            motor_a = 224
        elif motor_a == 32:
            motor_a = 223
        elif motor_a == 33:
            motor_a = 222
        elif motor_a == 34:
            motor_a = 221
        elif motor_a == 35:
            motor_a = 220
        elif motor_a == 36:
            motor_a = 219
        elif motor_a == 37:
            motor_a = 218
        elif motor_a == 38:
            motor_a = 217
        elif motor_a == 39:
            motor_a = 216
        elif motor_a == 40:
            motor_a = 215
        elif motor_a == 41:
            motor_a = 214
        elif motor_a == 42:
            motor_a = 213
        elif motor_a == 43:
            motor_a = 212
        elif motor_a == 44:
            motor_a = 211
        elif motor_a == 45:
            motor_a = 210
        elif motor_a == 46:
            motor_a = 209
        elif motor_a == 47:
            motor_a = 208
        elif motor_a == 48:
            motor_a = 207
        elif motor_a == 49:
            motor_a = 206
        elif motor_a == 50:
            motor_a = 205
        elif motor_a == 51:
            motor_a = 204
        elif motor_a == 52:
            motor_a = 203
        elif motor_a == 53:
            motor_a = 202
        elif motor_a == 54:
            motor_a = 201
        elif motor_a == 55:
            motor_a = 200
        elif motor_a == 56:
            motor_a = 199
        elif motor_a == 57:
            motor_a = 198
        elif motor_a == 58:
            motor_a = 197
        elif motor_a == 59:
            motor_a = 196
        elif motor_a == 60:
            motor_a = 195
        elif motor_a == 61:
            motor_a = 194
        elif motor_a == 62:
            motor_a = 193
        elif motor_a == 63:
            motor_a = 192
        elif motor_a == 64:
            motor_a = 191
        elif motor_a == 65:
            motor_a = 190
        elif motor_a == 66:
            motor_a = 189
        elif motor_a == 67:
            motor_a = 188
        elif motor_a == 68:
            motor_a = 187
        elif motor_a == 69:
            motor_a = 186
        elif motor_a == 70:
            motor_a = 185
        elif motor_a == 71:
            motor_a = 184
        elif motor_a == 72:
            motor_a = 183
        elif motor_a == 73:
            motor_a = 182
        elif motor_a == 74:
            motor_a = 181
        elif motor_a == 75:
            motor_a = 180
        elif motor_a == 76:
            motor_a = 179
        elif motor_a == 77:
            motor_a = 178
        elif motor_a == 78:
            motor_a = 177
        elif motor_a == 79:
            motor_a = 176
        elif motor_a == 80:
            motor_a = 175
        elif motor_a == 81:
            motor_a = 174
        elif motor_a == 82:
            motor_a = 173
        elif motor_a == 83:
            motor_a = 172
        elif motor_a == 84:
            motor_a = 171
        elif motor_a == 85:
            motor_a = 170
        elif motor_a == 86:
            motor_a = 169
        elif motor_a == 87:
            motor_a = 168
        elif motor_a == 88:
            motor_a = 167
        elif motor_a == 89:
            motor_a = 166
        elif motor_a == 90:
            motor_a = 165
        elif motor_a == 91:
            motor_a = 164
        elif motor_a == 92:
            motor_a = 163
        elif motor_a == 93:
            motor_a = 162
        elif motor_a == 94:
            motor_a = 161
        elif motor_a == 95:
            motor_a = 160
        elif motor_a == 96:
            motor_a = 159
        elif motor_a == 97:
            motor_a = 158
        elif motor_a == 98:
            motor_a = 157
        elif motor_a == 99:
            motor_a = 156
        elif motor_a == 100:
            motor_a = 155
        elif motor_a == 101:
            motor_a = 154
        elif motor_a == 102:
            motor_a = 153
        elif motor_a == 103:
            motor_a = 152
        elif motor_a == 104:
            motor_a = 151
        elif motor_a == 105:
            motor_a = 150
        elif motor_a == 106:
            motor_a = 149
        elif motor_a == 107:
            motor_a = 148
        elif motor_a == 108:
            motor_a = 147
        elif motor_a == 109:
            motor_a = 146
        elif motor_a == 110:
            motor_a = 145
        elif motor_a == 111:
            motor_a = 144
        elif motor_a == 112:
            motor_a = 143
        elif motor_a == 113:
            motor_a = 142
        elif motor_a == 114:
            motor_a = 141
        elif motor_a == 115:
            motor_a = 140
        elif motor_a == 116:
            motor_a = 139
        elif motor_a == 117:
            motor_a = 138
        elif motor_a == 118:
            motor_a = 137
        elif motor_a == 119:
            motor_a = 136
        elif motor_a == 120:
            motor_a = 135
        elif motor_a == 121:
            motor_a = 134
        elif motor_a == 122:
            motor_a = 133
        elif motor_a == 123:
            motor_a = 132
        elif motor_a == 124:
            motor_a = 131
        elif motor_a == 125:
            motor_a = 130
        elif motor_a == 126:
            motor_a = 129
        elif motor_a == 127:
            motor_a = 128
        elif motor_a == 128:
            motor_a = 127
        elif motor_a == 129:
            motor_a = 126
        elif motor_a == 130:
            motor_a = 125
        elif motor_a == 131:
            motor_a = 124
        elif motor_a == 132:
            motor_a = 123
        elif motor_a == 133:
            motor_a = 122
        elif motor_a == 134:
            motor_a = 121
        elif motor_a == 135:
            motor_a = 120
        elif motor_a == 136:
            motor_a = 119
        elif motor_a == 137:
            motor_a = 118
        elif motor_a == 138:
            motor_a = 117
        elif motor_a == 139:
            motor_a = 116
        elif motor_a == 140:
            motor_a = 115
        elif motor_a == 141:
            motor_a = 114
        elif motor_a == 142:
            motor_a = 113
        elif motor_a == 143:
            motor_a = 112
        elif motor_a == 144:
            motor_a = 111
        elif motor_a == 145:
            motor_a = 110
        elif motor_a == 146:
            motor_a = 109
        elif motor_a == 147:
            motor_a = 108
        elif motor_a == 148:
            motor_a = 107
        elif motor_a == 149:
            motor_a = 106
        elif motor_a == 150:
            motor_a = 105
        elif motor_a == 151:
            motor_a = 104
        elif motor_a == 152:
            motor_a = 103
        elif motor_a == 153:
            motor_a = 102
        elif motor_a == 154:
            motor_a = 101
        elif motor_a == 155:
            motor_a = 100
        elif motor_a == 156:
            motor_a = 99
        elif motor_a == 157:
            motor_a = 98
        elif motor_a == 158:
            motor_a = 97
        elif motor_a == 159:
            motor_a = 96
        elif motor_a == 160:
            motor_a = 95
        elif motor_a == 161:
            motor_a = 94
        elif motor_a == 162:
            motor_a = 93
        elif motor_a == 163:
            motor_a = 92
        elif motor_a == 164:
            motor_a = 91
        elif motor_a == 165:
            motor_a = 90
        elif motor_a == 166:
            motor_a = 89
        elif motor_a == 167:
            motor_a = 88
        elif motor_a == 168:
            motor_a = 87
        elif motor_a == 169:
            motor_a = 86
        elif motor_a == 170:
            motor_a = 85
        elif motor_a == 171:
            motor_a = 84
        elif motor_a == 172:
            motor_a = 83
        elif motor_a == 173:
            motor_a = 82
        elif motor_a == 174:
            motor_a = 81
        elif motor_a == 175:
            motor_a = 80
        elif motor_a == 176:
            motor_a = 79
        elif motor_a == 177:
            motor_a = 78
        elif motor_a == 178:
            motor_a = 77
        elif motor_a == 179:
            motor_a = 76
        elif motor_a == 180:
            motor_a = 75
        elif motor_a == 181:
            motor_a = 74
        elif motor_a == 182:
            motor_a = 73
        elif motor_a == 183:
            motor_a = 72
        elif motor_a == 184:
            motor_a = 71
        elif motor_a == 185:
            motor_a = 70
        elif motor_a == 186:
            motor_a = 69
        elif motor_a == 187:
            motor_a = 68
        elif motor_a == 188:
            motor_a = 67
        elif motor_a == 189:
            motor_a = 66
        elif motor_a == 190:
            motor_a = 65
        elif motor_a == 191:
            motor_a = 64
        elif motor_a == 192:
            motor_a = 63
        elif motor_a == 193:
            motor_a = 62
        elif motor_a == 194:
            motor_a = 61
        elif motor_a == 195:
            motor_a = 60
        elif motor_a == 196:
            motor_a = 59
        elif motor_a == 197:
            motor_a = 58
        elif motor_a == 198:
            motor_a = 57
        elif motor_a == 199:
            motor_a = 56
        elif motor_a == 200:
            motor_a = 55
        elif motor_a == 201:
            motor_a = 54
        elif motor_a == 202:
            motor_a = 53
        elif motor_a == 203:
            motor_a = 52
        elif motor_a == 204:
            motor_a = 51
        elif motor_a == 205:
            motor_a = 50
        elif motor_a == 206:
            motor_a = 49
        elif motor_a == 207:
            motor_a = 48
        elif motor_a == 208:
            motor_a = 47
        elif motor_a == 209:
            motor_a = 46
        elif motor_a == 210:
            motor_a = 45
        elif motor_a == 211:
            motor_a = 44
        elif motor_a == 212:
            motor_a = 43
        elif motor_a == 213:
            motor_a = 42
        elif motor_a == 214:
            motor_a = 41
        elif motor_a == 215:
            motor_a = 40
        elif motor_a == 216:
            motor_a = 39
        elif motor_a == 217:
            motor_a = 38
        elif motor_a == 218:
            motor_a = 37
        elif motor_a == 219:
            motor_a = 36
        elif motor_a == 220:
            motor_a = 35
        elif motor_a == 221:
            motor_a = 34
        elif motor_a == 222:
            motor_a = 33
        elif motor_a == 223:
            motor_a = 32
        elif motor_a == 224:
            motor_a = 31
        elif motor_a == 225:
            motor_a = 30
        elif motor_a == 226:
            motor_a = 29
        elif motor_a == 227:
            motor_a = 28
        elif motor_a == 228:
            motor_a = 27
        elif motor_a == 229:
            motor_a = 26
        elif motor_a == 230:
            motor_a = 25
        elif motor_a == 231:
            motor_a = 24
        elif motor_a == 232:
            motor_a = 23
        elif motor_a == 233:
            motor_a = 22
        elif motor_a == 234:
            motor_a = 21
        elif motor_a == 235:
            motor_a = 20
        elif motor_a == 236:
            motor_a = 19
        elif motor_a == 237:
            motor_a = 18
        elif motor_a == 238:
            motor_a = 17
        elif motor_a == 239:
            motor_a = 16
        elif motor_a == 240:
            motor_a = 15
        elif motor_a == 241:
            motor_a = 14
        elif motor_a == 242:
            motor_a = 13
        elif motor_a == 243:
            motor_a = 12
        elif motor_a == 244:
            motor_a = 11
        elif motor_a == 245:
            motor_a = 10
        elif motor_a == 246:
            motor_a = 9
        elif motor_a == 247:
            motor_a = 8
        elif motor_a == 248:
            motor_a = 7
        elif motor_a == 249:
            motor_a = 6
        elif motor_a == 250:
            motor_a = 5
        elif motor_a == 251:
            motor_a = 4
        elif motor_a == 252:
            motor_a = 3
        elif motor_a == 253:
            motor_a = 2
        elif motor_a == 254:
            motor_a = 1
        elif motor_a == 255:
            motor_a = 0


    def invert_motb():
        if motor_b == 0:
            motor_b = 255
        elif motor_b == 1:
            motor_b = 254
        elif motor_b == 2:
            motor_b = 253
        elif motor_b == 3:
            motor_b = 252
        elif motor_b == 4:
            motor_b = 251
        elif motor_b == 5:
            motor_b = 250
        elif motor_b == 6:
            motor_b = 249
        elif motor_b == 7:
            motor_b = 248
        elif motor_b == 8:
            motor_b = 247
        elif motor_b == 9:
            motor_b = 246
        elif motor_b == 10:
            motor_b = 245
        elif motor_b == 11:
            motor_b = 244
        elif motor_b == 12:
            motor_b = 243
        elif motor_b == 13:
            motor_b = 242
        elif motor_b == 14:
            motor_b = 241
        elif motor_b == 15:
            motor_b = 240
        elif motor_b == 16:
            motor_b = 239
        elif motor_b == 17:
            motor_b = 238
        elif motor_b == 18:
            motor_b = 237
        elif motor_b == 19:
            motor_b = 236
        elif motor_b == 20:
            motor_b = 235
        elif motor_b == 21:
            motor_b = 234
        elif motor_b == 22:
            motor_b = 233
        elif motor_b == 23:
            motor_b = 232
        elif motor_b == 24:
            motor_b = 231
        elif motor_b == 25:
            motor_b = 230
        elif motor_b == 26:
            motor_b = 229
        elif motor_b == 27:
            motor_b = 228
        elif motor_b == 28:
            motor_b = 227
        elif motor_b == 29:
            motor_b = 226
        elif motor_b == 30:
            motor_b = 225
        elif motor_b == 31:
            motor_b = 224
        elif motor_b == 32:
            motor_b = 223
        elif motor_b == 33:
            motor_b = 222
        elif motor_b == 34:
            motor_b = 221
        elif motor_b == 35:
            motor_b = 220
        elif motor_b == 36:
            motor_b = 219
        elif motor_b == 37:
            motor_b = 218
        elif motor_b == 38:
            motor_b = 217
        elif motor_b == 39:
            motor_b = 216
        elif motor_b == 40:
            motor_b = 215
        elif motor_b == 41:
            motor_b = 214
        elif motor_b == 42:
            motor_b = 213
        elif motor_b == 43:
            motor_b = 212
        elif motor_b == 44:
            motor_b = 211
        elif motor_b == 45:
            motor_b = 210
        elif motor_b == 46:
            motor_b = 209
        elif motor_b == 47:
            motor_b = 208
        elif motor_b == 48:
            motor_b = 207
        elif motor_b == 49:
            motor_b = 206
        elif motor_b == 50:
            motor_b = 205
        elif motor_b == 51:
            motor_b = 204
        elif motor_b == 52:
            motor_b = 203
        elif motor_b == 53:
            motor_b = 202
        elif motor_b == 54:
            motor_b = 201
        elif motor_b == 55:
            motor_b = 200
        elif motor_b == 56:
            motor_b = 199
        elif motor_b == 57:
            motor_b = 198
        elif motor_b == 58:
            motor_b = 197
        elif motor_b == 59:
            motor_b = 196
        elif motor_b == 60:
            motor_b = 195
        elif motor_b == 61:
            motor_b = 194
        elif motor_b == 62:
            motor_b = 193
        elif motor_b == 63:
            motor_b = 192
        elif motor_b == 64:
            motor_b = 191
        elif motor_b == 65:
            motor_b = 190
        elif motor_b == 66:
            motor_b = 189
        elif motor_b == 67:
            motor_b = 188
        elif motor_b == 68:
            motor_b = 187
        elif motor_b == 69:
            motor_b = 186
        elif motor_b == 70:
            motor_b = 185
        elif motor_b == 71:
            motor_b = 184
        elif motor_b == 72:
            motor_b = 183
        elif motor_b == 73:
            motor_b = 182
        elif motor_b == 74:
            motor_b = 181
        elif motor_b == 75:
            motor_b = 180
        elif motor_b == 76:
            motor_b = 179
        elif motor_b == 77:
            motor_b = 178
        elif motor_b == 78:
            motor_b = 177
        elif motor_b == 79:
            motor_b = 176
        elif motor_b == 80:
            motor_b = 175
        elif motor_b == 81:
            motor_b = 174
        elif motor_b == 82:
            motor_b = 173
        elif motor_b == 83:
            motor_b = 172
        elif motor_b == 84:
            motor_b = 171
        elif motor_b == 85:
            motor_b = 170
        elif motor_b == 86:
            motor_b = 169
        elif motor_b == 87:
            motor_b = 168
        elif motor_b == 88:
            motor_b = 167
        elif motor_b == 89:
            motor_b = 166
        elif motor_b == 90:
            motor_b = 165
        elif motor_b == 91:
            motor_b = 164
        elif motor_b == 92:
            motor_b = 163
        elif motor_b == 93:
            motor_b = 162
        elif motor_b == 94:
            motor_b = 161
        elif motor_b == 95:
            motor_b = 160
        elif motor_b == 96:
            motor_b = 159
        elif motor_b == 97:
            motor_b = 158
        elif motor_b == 98:
            motor_b = 157
        elif motor_b == 99:
            motor_b = 156
        elif motor_b == 100:
            motor_b = 155
        elif motor_b == 101:
            motor_b = 154
        elif motor_b == 102:
            motor_b = 153
        elif motor_b == 103:
            motor_b = 152
        elif motor_b == 104:
            motor_b = 151
        elif motor_b == 105:
            motor_b = 150
        elif motor_b == 106:
            motor_b = 149
        elif motor_b == 107:
            motor_b = 148
        elif motor_b == 108:
            motor_b = 147
        elif motor_b == 109:
            motor_b = 146
        elif motor_b == 110:
            motor_b = 145
        elif motor_b == 111:
            motor_b = 144
        elif motor_b == 112:
            motor_b = 143
        elif motor_b == 113:
            motor_b = 142
        elif motor_b == 114:
            motor_b = 141
        elif motor_b == 115:
            motor_b = 140
        elif motor_b == 116:
            motor_b = 139
        elif motor_b == 117:
            motor_b = 138
        elif motor_b == 118:
            motor_b = 137
        elif motor_b == 119:
            motor_b = 136
        elif motor_b == 120:
            motor_b = 135
        elif motor_b == 121:
            motor_b = 134
        elif motor_b == 122:
            motor_b = 133
        elif motor_b == 123:
            motor_b = 132
        elif motor_b == 124:
            motor_b = 131
        elif motor_b == 125:
            motor_b = 130
        elif motor_b == 126:
            motor_b = 129
        elif motor_b == 127:
            motor_b = 128
        elif motor_b == 128:
            motor_b = 127
        elif motor_b == 129:
            motor_b = 126
        elif motor_b == 130:
            motor_b = 125
        elif motor_b == 131:
            motor_b = 124
        elif motor_b == 132:
            motor_b = 123
        elif motor_b == 133:
            motor_b = 122
        elif motor_b == 134:
            motor_b = 121
        elif motor_b == 135:
            motor_b = 120
        elif motor_b == 136:
            motor_b = 119
        elif motor_b == 137:
            motor_b = 118
        elif motor_b == 138:
            motor_b = 117
        elif motor_b == 139:
            motor_b = 116
        elif motor_b == 140:
            motor_b = 115
        elif motor_b == 141:
            motor_b = 114
        elif motor_b == 142:
            motor_b = 113
        elif motor_b == 143:
            motor_b = 112
        elif motor_b == 144:
            motor_b = 111
        elif motor_b == 145:
            motor_b = 110
        elif motor_b == 146:
            motor_b = 109
        elif motor_b == 147:
            motor_b = 108
        elif motor_b == 148:
            motor_b = 107
        elif motor_b == 149:
            motor_b = 106
        elif motor_b == 150:
            motor_b = 105
        elif motor_b == 151:
            motor_b = 104
        elif motor_b == 152:
            motor_b = 103
        elif motor_b == 153:
            motor_b = 102
        elif motor_b == 154:
            motor_b = 101
        elif motor_b == 155:
            motor_b = 100
        elif motor_b == 156:
            motor_b = 99
        elif motor_b == 157:
            motor_b = 98
        elif motor_b == 158:
            motor_b = 97
        elif motor_b == 159:
            motor_b = 96
        elif motor_b == 160:
            motor_b = 95
        elif motor_b == 161:
            motor_b = 94
        elif motor_b == 162:
            motor_b = 93
        elif motor_b == 163:
            motor_b = 92
        elif motor_b == 164:
            motor_b = 91
        elif motor_b == 165:
            motor_b = 90
        elif motor_b == 166:
            motor_b = 89
        elif motor_b == 167:
            motor_b = 88
        elif motor_b == 168:
            motor_b = 87
        elif motor_b == 169:
            motor_b = 86
        elif motor_b == 170:
            motor_b = 85
        elif motor_b == 171:
            motor_b = 84
        elif motor_b == 172:
            motor_b = 83
        elif motor_b == 173:
            motor_b = 82
        elif motor_b == 174:
            motor_b = 81
        elif motor_b == 175:
            motor_b = 80
        elif motor_b == 176:
            motor_b = 79
        elif motor_b == 177:
            motor_b = 78
        elif motor_b == 178:
            motor_b = 77
        elif motor_b == 179:
            motor_b = 76
        elif motor_b == 180:
            motor_b = 75
        elif motor_b == 181:
            motor_b = 74
        elif motor_b == 182:
            motor_b = 73
        elif motor_b == 183:
            motor_b = 72
        elif motor_b == 184:
            motor_b = 71
        elif motor_b == 185:
            motor_b = 70
        elif motor_b == 186:
            motor_b = 69
        elif motor_b == 187:
            motor_b = 68
        elif motor_b == 188:
            motor_b = 67
        elif motor_b == 189:
            motor_b = 66
        elif motor_b == 190:
            motor_b = 65
        elif motor_b == 191:
            motor_b = 64
        elif motor_b == 192:
            motor_b = 63
        elif motor_b == 193:
            motor_b = 62
        elif motor_b == 194:
            motor_b = 61
        elif motor_b == 195:
            motor_b = 60
        elif motor_b == 196:
            motor_b = 59
        elif motor_b == 197:
            motor_b = 58
        elif motor_b == 198:
            motor_b = 57
        elif motor_b == 199:
            motor_b = 56
        elif motor_b == 200:
            motor_b = 55
        elif motor_b == 201:
            motor_b = 54
        elif motor_b == 202:
            motor_b = 53
        elif motor_b == 203:
            motor_b = 52
        elif motor_b == 204:
            motor_b = 51
        elif motor_b == 205:
            motor_b = 50
        elif motor_b == 206:
            motor_b = 49
        elif motor_b == 207:
            motor_b = 48
        elif motor_b == 208:
            motor_b = 47
        elif motor_b == 209:
            motor_b = 46
        elif motor_b == 210:
            motor_b = 45
        elif motor_b == 211:
            motor_b = 44
        elif motor_b == 212:
            motor_b = 43
        elif motor_b == 213:
            motor_b = 42
        elif motor_b == 214:
            motor_b = 41
        elif motor_b == 215:
            motor_b = 40
        elif motor_b == 216:
            motor_b = 39
        elif motor_b == 217:
            motor_b = 38
        elif motor_b == 218:
            motor_b = 37
        elif motor_b == 219:
            motor_b = 36
        elif motor_b == 220:
            motor_b = 35
        elif motor_b == 221:
            motor_b = 34
        elif motor_b == 222:
            motor_b = 33
        elif motor_b == 223:
            motor_b = 32
        elif motor_b == 224:
            motor_b = 31
        elif motor_b == 225:
            motor_b = 30
        elif motor_b == 226:
            motor_b = 29
        elif motor_b == 227:
            motor_b = 28
        elif motor_b == 228:
            motor_b = 27
        elif motor_b == 229:
            motor_b = 26
        elif motor_b == 230:
            motor_b = 25
        elif motor_b == 231:
            motor_b = 24
        elif motor_b == 232:
            motor_b = 23
        elif motor_b == 233:
            motor_b = 22
        elif motor_b == 234:
            motor_b = 21
        elif motor_b == 235:
            motor_b = 20
        elif motor_b == 236:
            motor_b = 19
        elif motor_b == 237:
            motor_b = 18
        elif motor_b == 238:
            motor_b = 17
        elif motor_b == 239:
            motor_b = 16
        elif motor_b == 240:
            motor_b = 15
        elif motor_b == 241:
            motor_b = 14
        elif motor_b == 242:
            motor_b = 13
        elif motor_b == 243:
            motor_b = 12
        elif motor_b == 244:
            motor_b = 11
        elif motor_b == 245:
            motor_b = 10
        elif motor_b == 246:
            motor_b = 9
        elif motor_b == 247:
            motor_b = 8
        elif motor_b == 248:
            motor_b = 7
        elif motor_b == 249:
            motor_b = 6
        elif motor_b == 250:
            motor_b = 5
        elif motor_b == 251:
            motor_b = 4
        elif motor_b == 252:
            motor_b = 3
        elif motor_b == 253:
            motor_b = 2
        elif motor_b == 254:
            motor_b = 1
        elif motor_b == 255:
            motor_b = 0





        
