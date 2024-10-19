import random
import time
import asyncio

class Solarcell:
    def __init__(self, id):
        self.id = id
        self.hardware_readtime = random.randint(1, 3)
        print(f"Solarcell {id} hardware speed: {self.hardware_readtime} ")

    async def r_voltage(self):  
        voltage = round(random.uniform(3.2, 6.0), 2)
        await asyncio.sleep(self.hardware_readtime)  
        return voltage

async def read_from_solar_cells(solar_cells):
    try:
        while True:
            tasks = []
            for solar_cell in solar_cells:
                task = asyncio.create_task(log_voltage(solar_cell))  
                tasks.append(task)
            await asyncio.gather(*tasks)  
    except KeyboardInterrupt:
        print("\nโปรแกรมหยุดทำงาน")

async def log_voltage(solar_cell):
    voltage = await solar_cell.r_voltage()  
    print(f"{time.ctime()} Solar_cell #{solar_cell.id} Voltage: {voltage} V")

if __name__ == "__main__":
    num_cells = 5
    print(f"จำนวนแผงโซล่าเซลที่สร้าง: {num_cells}")

    solar_cells = [Solarcell(i+1) for i in range(num_cells)]
    asyncio.run(read_from_solar_cells(solar_cells))  
    
    