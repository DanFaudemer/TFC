################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ../makefile.local

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS_QUOTED += \
"../Sources/chrono.c" \
"../Sources/distantio.c" \
"../Sources/logger.c" \
"../Sources/main.c" \
"../Sources/protocol.c" \
"../Sources/sa_mtb.c" \
"../Sources/serial.c" \
"../Sources/signalProcessing.c" \

C_SRCS += \
../Sources/chrono.c \
../Sources/distantio.c \
../Sources/logger.c \
../Sources/main.c \
../Sources/protocol.c \
../Sources/sa_mtb.c \
../Sources/serial.c \
../Sources/signalProcessing.c \

OBJS += \
./Sources/chrono.o \
./Sources/distantio.o \
./Sources/logger.o \
./Sources/main.o \
./Sources/protocol.o \
./Sources/sa_mtb.o \
./Sources/serial.o \
./Sources/signalProcessing.o \

OBJS_QUOTED += \
"./Sources/chrono.o" \
"./Sources/distantio.o" \
"./Sources/logger.o" \
"./Sources/main.o" \
"./Sources/protocol.o" \
"./Sources/sa_mtb.o" \
"./Sources/serial.o" \
"./Sources/signalProcessing.o" \

C_DEPS += \
./Sources/chrono.d \
./Sources/distantio.d \
./Sources/logger.d \
./Sources/main.d \
./Sources/protocol.d \
./Sources/sa_mtb.d \
./Sources/serial.d \
./Sources/signalProcessing.d \

OBJS_OS_FORMAT += \
./Sources/chrono.o \
./Sources/distantio.o \
./Sources/logger.o \
./Sources/main.o \
./Sources/protocol.o \
./Sources/sa_mtb.o \
./Sources/serial.o \
./Sources/signalProcessing.o \

C_DEPS_QUOTED += \
"./Sources/chrono.d" \
"./Sources/distantio.d" \
"./Sources/logger.d" \
"./Sources/main.d" \
"./Sources/protocol.d" \
"./Sources/sa_mtb.d" \
"./Sources/serial.d" \
"./Sources/signalProcessing.d" \


# Each subdirectory must supply rules for building sources it contributes
Sources/chrono.o: ../Sources/chrono.c
	@echo 'Building file: $<'
	@echo 'Executing target #1 $<'
	@echo 'Invoking: ARM Ltd Windows GCC C Compiler'
	"$(ARMSourceryDirEnv)/arm-none-eabi-gcc" "$<" @"Sources/chrono.args" -Wa,-adhlns="$@.lst" -MMD -MP -MF"$(@:%.o=%.d)" -o"Sources/chrono.o"
	@echo 'Finished building: $<'
	@echo ' '

Sources/distantio.o: ../Sources/distantio.c
	@echo 'Building file: $<'
	@echo 'Executing target #2 $<'
	@echo 'Invoking: ARM Ltd Windows GCC C Compiler'
	"$(ARMSourceryDirEnv)/arm-none-eabi-gcc" "$<" @"Sources/distantio.args" -Wa,-adhlns="$@.lst" -MMD -MP -MF"$(@:%.o=%.d)" -o"Sources/distantio.o"
	@echo 'Finished building: $<'
	@echo ' '

Sources/logger.o: ../Sources/logger.c
	@echo 'Building file: $<'
	@echo 'Executing target #3 $<'
	@echo 'Invoking: ARM Ltd Windows GCC C Compiler'
	"$(ARMSourceryDirEnv)/arm-none-eabi-gcc" "$<" @"Sources/logger.args" -Wa,-adhlns="$@.lst" -MMD -MP -MF"$(@:%.o=%.d)" -o"Sources/logger.o"
	@echo 'Finished building: $<'
	@echo ' '

Sources/main.o: ../Sources/main.c
	@echo 'Building file: $<'
	@echo 'Executing target #4 $<'
	@echo 'Invoking: ARM Ltd Windows GCC C Compiler'
	"$(ARMSourceryDirEnv)/arm-none-eabi-gcc" "$<" @"Sources/main.args" -Wa,-adhlns="$@.lst" -MMD -MP -MF"$(@:%.o=%.d)" -o"Sources/main.o"
	@echo 'Finished building: $<'
	@echo ' '

Sources/protocol.o: ../Sources/protocol.c
	@echo 'Building file: $<'
	@echo 'Executing target #5 $<'
	@echo 'Invoking: ARM Ltd Windows GCC C Compiler'
	"$(ARMSourceryDirEnv)/arm-none-eabi-gcc" "$<" @"Sources/protocol.args" -Wa,-adhlns="$@.lst" -MMD -MP -MF"$(@:%.o=%.d)" -o"Sources/protocol.o"
	@echo 'Finished building: $<'
	@echo ' '

Sources/sa_mtb.o: ../Sources/sa_mtb.c
	@echo 'Building file: $<'
	@echo 'Executing target #6 $<'
	@echo 'Invoking: ARM Ltd Windows GCC C Compiler'
	"$(ARMSourceryDirEnv)/arm-none-eabi-gcc" "$<" @"Sources/sa_mtb.args" -Wa,-adhlns="$@.lst" -MMD -MP -MF"$(@:%.o=%.d)" -o"Sources/sa_mtb.o"
	@echo 'Finished building: $<'
	@echo ' '

Sources/serial.o: ../Sources/serial.c
	@echo 'Building file: $<'
	@echo 'Executing target #7 $<'
	@echo 'Invoking: ARM Ltd Windows GCC C Compiler'
	"$(ARMSourceryDirEnv)/arm-none-eabi-gcc" "$<" @"Sources/serial.args" -Wa,-adhlns="$@.lst" -MMD -MP -MF"$(@:%.o=%.d)" -o"Sources/serial.o"
	@echo 'Finished building: $<'
	@echo ' '

Sources/signalProcessing.o: ../Sources/signalProcessing.c
	@echo 'Building file: $<'
	@echo 'Executing target #8 $<'
	@echo 'Invoking: ARM Ltd Windows GCC C Compiler'
	"$(ARMSourceryDirEnv)/arm-none-eabi-gcc" "$<" @"Sources/signalProcessing.args" -Wa,-adhlns="$@.lst" -MMD -MP -MF"$(@:%.o=%.d)" -o"Sources/signalProcessing.o"
	@echo 'Finished building: $<'
	@echo ' '


