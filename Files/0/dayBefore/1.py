def dayBefore(ymd):
    def isleap (year):
        return \
            True  if not year % 400 else \
            False if not year % 100 else \
            True  if not year %   4 else \
            False
    DAY_BEFORE_FIRST_OF_MONTH = (
    #   ( M,  D, X) ## X = NEGATIVE DELTA-Y
        None, #0: NO MONTH
        (12, 31, 1), #1: JANUARY
        ( 1, 31, 0), #2: FEBRUARY
        None, #3: MARCH (SPECIAL CASE)
        ( 3, 31, 0),
        ( 4, 30, 0),
        ( 5, 31, 0),
        ( 6, 30, 0),
        ( 7, 31, 0),
        ( 8, 31, 0),
        ( 9, 30, 0),
        (10, 31, 0),
        (11, 30, 0))
    def dayBeforeMarch1(year):
        return year, 2, ( 29 if isleap(year) else 28 )
    def dayBeforeFirstOfTheMonthIfNotMarch1(ym):
        m, d, dy = DAY_BEFORE_FIRST_OF_MONTH[ym[1]]
        return ym[0] - dy, m, d
    def dayBefore_(ymd):
        y, m, d = ymd
        return \
            (y, m, d - 1) if 1 < d else \
            dayBeforeMarch1(y) if (m, d) == (3, 1) else \
            dayBeforeFirstOfTheMonthIfNotMarch1(ymd[:2])
    return dayBefore_(ymd)
