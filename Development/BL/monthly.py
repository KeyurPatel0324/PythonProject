

class monthlycost:
    def __init__(self):
        super().__init__()
        self.corporte = None
        self.borewell = None
        self.borewell_charge = 1.5
        self.corportecharge  = 1
        self.aprt2 = 3
        self.aprt3 = 5
        self.perliter = 10
        self.aprt2liter = 900
        self.aprt3liter = 1500
        self.brwusedwater = 0
        self.crpusedwater = 0
        self.bill = 0
        self.usedwater = 0
        self.gues_used_water = 0


    def MonthlyData(self,json):
        try:
            watersupply = json['allotedwater']
            add_guest = json['add_guest']
            apprt_type = watersupply['appartment']
            ratio = watersupply['ratio']
            self.corporte = int(ratio.split(':')[0])
            self.borewell = int(ratio.split(':')[1])
            self.total_guest = 0
            for i in add_guest:
                self.total_guest += i['ag']
            if apprt_type == 3:
                self.corportecost(self.aprt3liter)
            else:
                self.corportecost(self.aprt2liter)
            return {'bill':int(self.bill),'total_water':self.usedwater}
        except BaseException as e:
            raise e

    def corportecost(self,aprt):
        try:
            extrabill = 0
            self.crpusedwater = int(aprt/self.corporte)
            self.brwusedwater = int(aprt/self.borewell)
            if self.total_guest > 0:

                self.gues_used_water = self.total_guest * self.perliter * 30
            self.usedwater = self.crpusedwater + self.brwusedwater + self.gues_used_water
            if self.usedwater > aprt :
                extrawater = self.usedwater - aprt


                if extrawater > 3000:
                    remainwater = extrawater - 3000
                    extrabill = 500 * 2 + 1000 * 3 + 1500 * 5 + remainwater * 8
                elif extrawater > 1500 and extrawater <=3000:
                    remainwater = extrawater - 1500
                    extrabill = 500 * 2 + 1000 * 3 + remainwater * 5
                elif extrawater > 500 and extrawater <= 1500:
                    remainwater = extrawater - 500
                    extrabill = 500 * 2 + remainwater * 3
                else:
                    extrabill = extrawater * 2

            self.bill = self.crpusedwater * self.corportecharge + self.brwusedwater * self.borewell_charge + extrabill

        except BaseException as e:
            raise

# aa = monthlycost()
# data = {'allotedwater': {'ratio': '1:5', 'appartment': 3}, 'add_guest': [{'ag': 2}]}
# aa.MonthlyData(data)