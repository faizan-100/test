import numpy as np

class SwimmingVioletBull(QCAlgorithm):

    def Initialize(self):
        self.SetCash(100000)  # Set Strategy Cash
        # self.AddEquity("SPY", Resolution.Minute)
        self.SetStartDate(2022, 1, 23) # set start date
        self.SetEndDate(2022, 3, 23) # set end date

        self.symbol = self.AddEquity("SPY", Resolution.Daily).Symbol
# etf SPY is the security which tracks the SNP 500
        self.lookback = 20
# algorithm dynamically changes the lookback length based on volatility
        self.ceiling, self.floor = 30, 10
#To make sure the lookback length doesnt get too big or too small

        self.intialStopRisk = 0.98     # indicates how close the first stop loss will be to the securities price, allows for a 2% loss before it gets  hit
        self.trailingStopRisk = 0.9    # indicates how close the stock will follow the assets price, it will trade at a price by 10%

        self.Schedule.On(self.DateRules.EveryDay(self.symbol), \
                         self.TimeRules.AfterMarketOpen(self.symbol, 20), \
                         Action(self.EveryMarketOpen))


    def OnData(self, data):
        self.Plot("Data Chart", self.symbol, self.Securities[self.symbol].Close)

    def EveryMarketOpen(self):
        # determines the lookback length for the breakout
        close = self.Histroy(self.symbol, 31, Resolution.Daily)["close"]
        todayvol = np.std(close[1:31]) # calculates volatility by taking standard deviation of the closing price over the last 30 days, first taking the current day
        yesterdayvol = np.std(close[0:30])  # then taking the previous day
        deltavol = (todayvol - yesterdayvol) / todayvol   # then calculate the normalised difference
        self.lookback = round(self.lookback * (1 + deltavol)) # ensures the look back length increases as volatility increases and vice versa

        if self.lookback > self.ceiling:   #  makes sure the lookback lenght is within the upper and lower
            self.lookback = self.ceiling
        elif self.lookback < self.floor:
            self.lookback = self.floor

        self.high = self.History(self.symbol, self.lookback, Resolution.Daily)["high"] # checks if a breakout is happening bby checking the daily price highs from the lookabck lenght

        if not self.Securities[self.symbol].Invested and \
                self.Securities[self.symbol].Close >= max(self.high[:-1]):
            self.SetHoldings(self.symbol, 1)
            self.breakoutlvl = max(self.high[:-1])
            self.highestPrice = self.breakoutlvl

        if self.Securities[self.symbol].Invested:
            if not self.Transaction.GetOpenOrders(self.symbol):
                self.stopMarketTicket = self.StopMarketOrder(self.symbol, \
                                                             -self.Portfloio[self.symbol].Quantity, \
                                                             self.intitialStopRisk * self.breakoutlvl)
            if self.Securities[self.symbol].Close > self.highestPrice and \
                    self.initialStopRisk * self.breakoutlvl < self.Securities[self.symbol].Close * self.trailingStopRisk:
                self.highestPrice = self.Secirities[self.symbol].Close * self.trailingStopRisk

                self.Debug(updateFields.StopPrice)

            self.Plot("Data Chart", "Stop Price", self.stopMarketTicket.Get(OrderField.StopPrice))






        '''OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.
            Arguments:
                data: Slice object keyed by symbol containing the stock data
        '''

        # if not self.Portfolio.Invested:
        #    self.SetHoldings("SPY", 1)