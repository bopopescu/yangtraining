""" Cisco_IOS_XR_infra_infra_clock_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-infra\-clock package configuration.

This module contains definitions
for the following management objects\:
  clock\: Configure time\-of\-day clock

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class ClockMonth(Enum):
    """
    ClockMonth

    Clock month

    .. data:: january = 0

    	January

    .. data:: february = 1

    	February

    .. data:: march = 2

    	March

    .. data:: april = 3

    	April

    .. data:: may = 4

    	May

    .. data:: june = 5

    	June

    .. data:: july = 6

    	July

    .. data:: august = 7

    	August

    .. data:: september = 8

    	September

    .. data:: october = 9

    	October

    .. data:: november = 10

    	November

    .. data:: december = 11

    	December

    """

    january = Enum.YLeaf(0, "january")

    february = Enum.YLeaf(1, "february")

    march = Enum.YLeaf(2, "march")

    april = Enum.YLeaf(3, "april")

    may = Enum.YLeaf(4, "may")

    june = Enum.YLeaf(5, "june")

    july = Enum.YLeaf(6, "july")

    august = Enum.YLeaf(7, "august")

    september = Enum.YLeaf(8, "september")

    october = Enum.YLeaf(9, "october")

    november = Enum.YLeaf(10, "november")

    december = Enum.YLeaf(11, "december")


class ClockSummerTimeMode(Enum):
    """
    ClockSummerTimeMode

    Clock summer time mode

    .. data:: recurring = 0

    	Recurring summer time

    .. data:: date = 1

    	Absolute summer time

    """

    recurring = Enum.YLeaf(0, "recurring")

    date = Enum.YLeaf(1, "date")



class Clock(Entity):
    """
    Configure time\-of\-day clock
    
    .. attribute:: summer_time
    
    	Configure summer (daylight savings) time
    	**type**\:   :py:class:`SummerTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_cfg.Clock.SummerTime>`
    
    	**presence node**\: True
    
    .. attribute:: time_zone
    
    	Configure time zone
    	**type**\:   :py:class:`TimeZone <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_cfg.Clock.TimeZone>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'infra-infra-clock-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Clock, self).__init__()
        self._top_entity = None

        self.yang_name = "clock"
        self.yang_parent_name = "Cisco-IOS-XR-infra-infra-clock-cfg"

        self.summer_time = None
        self._children_name_map["summer_time"] = "summer-time"
        self._children_yang_names.add("summer-time")

        self.time_zone = None
        self._children_name_map["time_zone"] = "time-zone"
        self._children_yang_names.add("time-zone")


    class SummerTime(Entity):
        """
        Configure summer (daylight savings) time
        
        .. attribute:: end_hour
        
        	Hour to end 
        	**type**\:  int
        
        	**range:** 0..23
        
        .. attribute:: end_minute
        
        	Minute to end 
        	**type**\:  int
        
        	**range:** 0..59
        
        .. attribute:: end_month
        
        	 Month to end 
        	**type**\:   :py:class:`ClockMonth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_cfg.ClockMonth>`
        
        .. attribute:: end_week_number_or_end_date
        
        	If Mode is set to 'Recurring' specify Week number of the Month to end (first and last strings are not allowed as they are in CLI), if Mode is set to 'Date' specify Date to End
        	**type**\:  int
        
        	**range:** 1..31
        
        .. attribute:: end_weekday_or_end_year
        
        	If Mode is set to 'Recurring' specify Weekday to end , if Mode is set to 'Date' specify Year to end
        	**type**\:  int
        
        	**range:** 0..2035
        
        .. attribute:: mode
        
        	Summer time mode
        	**type**\:   :py:class:`ClockSummerTimeMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_cfg.ClockSummerTimeMode>`
        
        	**mandatory**\: True
        
        .. attribute:: offset
        
        	Offset to add in minutes 
        	**type**\:  int
        
        	**range:** 1..1440
        
        	**units**\: minute
        
        .. attribute:: start_hour
        
        	Hour to start 
        	**type**\:  int
        
        	**range:** 0..23
        
        .. attribute:: start_minute
        
        	Minute to start 
        	**type**\:  int
        
        	**range:** 0..59
        
        .. attribute:: start_month
        
        	 Month to start 
        	**type**\:   :py:class:`ClockMonth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_cfg.ClockMonth>`
        
        .. attribute:: start_week_number_or_start_date
        
        	 If Mode is set to 'Recurring' specify Week number of the Month to start (first and last strings are not allowed as they are in CLI) , if Mode is set to 'Date' specify Date to start 
        	**type**\:  int
        
        	**range:** 1..31
        
        .. attribute:: start_weekday_or_start_year
        
        	 If Mode is set to 'Recurring' specify Weekday to start , if Mode is set to 'Date' specify Year to start 
        	**type**\:  int
        
        	**range:** 0..2035
        
        .. attribute:: time_zone_name
        
        	Name of time zone in summer
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-infra-clock-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Clock.SummerTime, self).__init__()

            self.yang_name = "summer-time"
            self.yang_parent_name = "clock"
            self.is_presence_container = True

            self.end_hour = YLeaf(YType.uint32, "end-hour")

            self.end_minute = YLeaf(YType.uint32, "end-minute")

            self.end_month = YLeaf(YType.enumeration, "end-month")

            self.end_week_number_or_end_date = YLeaf(YType.uint32, "end-week-number-or-end-date")

            self.end_weekday_or_end_year = YLeaf(YType.uint32, "end-weekday-or-end-year")

            self.mode = YLeaf(YType.enumeration, "mode")

            self.offset = YLeaf(YType.uint32, "offset")

            self.start_hour = YLeaf(YType.uint32, "start-hour")

            self.start_minute = YLeaf(YType.uint32, "start-minute")

            self.start_month = YLeaf(YType.enumeration, "start-month")

            self.start_week_number_or_start_date = YLeaf(YType.uint32, "start-week-number-or-start-date")

            self.start_weekday_or_start_year = YLeaf(YType.uint32, "start-weekday-or-start-year")

            self.time_zone_name = YLeaf(YType.str, "time-zone-name")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("end_hour",
                            "end_minute",
                            "end_month",
                            "end_week_number_or_end_date",
                            "end_weekday_or_end_year",
                            "mode",
                            "offset",
                            "start_hour",
                            "start_minute",
                            "start_month",
                            "start_week_number_or_start_date",
                            "start_weekday_or_start_year",
                            "time_zone_name") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Clock.SummerTime, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Clock.SummerTime, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.end_hour.is_set or
                self.end_minute.is_set or
                self.end_month.is_set or
                self.end_week_number_or_end_date.is_set or
                self.end_weekday_or_end_year.is_set or
                self.mode.is_set or
                self.offset.is_set or
                self.start_hour.is_set or
                self.start_minute.is_set or
                self.start_month.is_set or
                self.start_week_number_or_start_date.is_set or
                self.start_weekday_or_start_year.is_set or
                self.time_zone_name.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.end_hour.yfilter != YFilter.not_set or
                self.end_minute.yfilter != YFilter.not_set or
                self.end_month.yfilter != YFilter.not_set or
                self.end_week_number_or_end_date.yfilter != YFilter.not_set or
                self.end_weekday_or_end_year.yfilter != YFilter.not_set or
                self.mode.yfilter != YFilter.not_set or
                self.offset.yfilter != YFilter.not_set or
                self.start_hour.yfilter != YFilter.not_set or
                self.start_minute.yfilter != YFilter.not_set or
                self.start_month.yfilter != YFilter.not_set or
                self.start_week_number_or_start_date.yfilter != YFilter.not_set or
                self.start_weekday_or_start_year.yfilter != YFilter.not_set or
                self.time_zone_name.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "summer-time" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-infra-clock-cfg:clock/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.end_hour.is_set or self.end_hour.yfilter != YFilter.not_set):
                leaf_name_data.append(self.end_hour.get_name_leafdata())
            if (self.end_minute.is_set or self.end_minute.yfilter != YFilter.not_set):
                leaf_name_data.append(self.end_minute.get_name_leafdata())
            if (self.end_month.is_set or self.end_month.yfilter != YFilter.not_set):
                leaf_name_data.append(self.end_month.get_name_leafdata())
            if (self.end_week_number_or_end_date.is_set or self.end_week_number_or_end_date.yfilter != YFilter.not_set):
                leaf_name_data.append(self.end_week_number_or_end_date.get_name_leafdata())
            if (self.end_weekday_or_end_year.is_set or self.end_weekday_or_end_year.yfilter != YFilter.not_set):
                leaf_name_data.append(self.end_weekday_or_end_year.get_name_leafdata())
            if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mode.get_name_leafdata())
            if (self.offset.is_set or self.offset.yfilter != YFilter.not_set):
                leaf_name_data.append(self.offset.get_name_leafdata())
            if (self.start_hour.is_set or self.start_hour.yfilter != YFilter.not_set):
                leaf_name_data.append(self.start_hour.get_name_leafdata())
            if (self.start_minute.is_set or self.start_minute.yfilter != YFilter.not_set):
                leaf_name_data.append(self.start_minute.get_name_leafdata())
            if (self.start_month.is_set or self.start_month.yfilter != YFilter.not_set):
                leaf_name_data.append(self.start_month.get_name_leafdata())
            if (self.start_week_number_or_start_date.is_set or self.start_week_number_or_start_date.yfilter != YFilter.not_set):
                leaf_name_data.append(self.start_week_number_or_start_date.get_name_leafdata())
            if (self.start_weekday_or_start_year.is_set or self.start_weekday_or_start_year.yfilter != YFilter.not_set):
                leaf_name_data.append(self.start_weekday_or_start_year.get_name_leafdata())
            if (self.time_zone_name.is_set or self.time_zone_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.time_zone_name.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "end-hour" or name == "end-minute" or name == "end-month" or name == "end-week-number-or-end-date" or name == "end-weekday-or-end-year" or name == "mode" or name == "offset" or name == "start-hour" or name == "start-minute" or name == "start-month" or name == "start-week-number-or-start-date" or name == "start-weekday-or-start-year" or name == "time-zone-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "end-hour"):
                self.end_hour = value
                self.end_hour.value_namespace = name_space
                self.end_hour.value_namespace_prefix = name_space_prefix
            if(value_path == "end-minute"):
                self.end_minute = value
                self.end_minute.value_namespace = name_space
                self.end_minute.value_namespace_prefix = name_space_prefix
            if(value_path == "end-month"):
                self.end_month = value
                self.end_month.value_namespace = name_space
                self.end_month.value_namespace_prefix = name_space_prefix
            if(value_path == "end-week-number-or-end-date"):
                self.end_week_number_or_end_date = value
                self.end_week_number_or_end_date.value_namespace = name_space
                self.end_week_number_or_end_date.value_namespace_prefix = name_space_prefix
            if(value_path == "end-weekday-or-end-year"):
                self.end_weekday_or_end_year = value
                self.end_weekday_or_end_year.value_namespace = name_space
                self.end_weekday_or_end_year.value_namespace_prefix = name_space_prefix
            if(value_path == "mode"):
                self.mode = value
                self.mode.value_namespace = name_space
                self.mode.value_namespace_prefix = name_space_prefix
            if(value_path == "offset"):
                self.offset = value
                self.offset.value_namespace = name_space
                self.offset.value_namespace_prefix = name_space_prefix
            if(value_path == "start-hour"):
                self.start_hour = value
                self.start_hour.value_namespace = name_space
                self.start_hour.value_namespace_prefix = name_space_prefix
            if(value_path == "start-minute"):
                self.start_minute = value
                self.start_minute.value_namespace = name_space
                self.start_minute.value_namespace_prefix = name_space_prefix
            if(value_path == "start-month"):
                self.start_month = value
                self.start_month.value_namespace = name_space
                self.start_month.value_namespace_prefix = name_space_prefix
            if(value_path == "start-week-number-or-start-date"):
                self.start_week_number_or_start_date = value
                self.start_week_number_or_start_date.value_namespace = name_space
                self.start_week_number_or_start_date.value_namespace_prefix = name_space_prefix
            if(value_path == "start-weekday-or-start-year"):
                self.start_weekday_or_start_year = value
                self.start_weekday_or_start_year.value_namespace = name_space
                self.start_weekday_or_start_year.value_namespace_prefix = name_space_prefix
            if(value_path == "time-zone-name"):
                self.time_zone_name = value
                self.time_zone_name.value_namespace = name_space
                self.time_zone_name.value_namespace_prefix = name_space_prefix


    class TimeZone(Entity):
        """
        Configure time zone
        
        .. attribute:: hour_offset
        
        	Hours offset from UTC
        	**type**\:  int
        
        	**range:** \-23..23
        
        	**mandatory**\: True
        
        	**units**\: hour
        
        .. attribute:: minute_offset
        
        	Minutes offset from UTC
        	**type**\:  int
        
        	**range:** 0..59
        
        	**units**\: minute
        
        	**default value**\: 0
        
        .. attribute:: time_zone_name
        
        	Name of time zone
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-infra-clock-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Clock.TimeZone, self).__init__()

            self.yang_name = "time-zone"
            self.yang_parent_name = "clock"
            self.is_presence_container = True

            self.hour_offset = YLeaf(YType.int32, "hour-offset")

            self.minute_offset = YLeaf(YType.uint32, "minute-offset")

            self.time_zone_name = YLeaf(YType.str, "time-zone-name")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("hour_offset",
                            "minute_offset",
                            "time_zone_name") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Clock.TimeZone, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Clock.TimeZone, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.hour_offset.is_set or
                self.minute_offset.is_set or
                self.time_zone_name.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.hour_offset.yfilter != YFilter.not_set or
                self.minute_offset.yfilter != YFilter.not_set or
                self.time_zone_name.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "time-zone" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-infra-clock-cfg:clock/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.hour_offset.is_set or self.hour_offset.yfilter != YFilter.not_set):
                leaf_name_data.append(self.hour_offset.get_name_leafdata())
            if (self.minute_offset.is_set or self.minute_offset.yfilter != YFilter.not_set):
                leaf_name_data.append(self.minute_offset.get_name_leafdata())
            if (self.time_zone_name.is_set or self.time_zone_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.time_zone_name.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "hour-offset" or name == "minute-offset" or name == "time-zone-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "hour-offset"):
                self.hour_offset = value
                self.hour_offset.value_namespace = name_space
                self.hour_offset.value_namespace_prefix = name_space_prefix
            if(value_path == "minute-offset"):
                self.minute_offset = value
                self.minute_offset.value_namespace = name_space
                self.minute_offset.value_namespace_prefix = name_space_prefix
            if(value_path == "time-zone-name"):
                self.time_zone_name = value
                self.time_zone_name.value_namespace = name_space
                self.time_zone_name.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.summer_time is not None) or
            (self.time_zone is not None))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.summer_time is not None and self.summer_time.has_operation()) or
            (self.time_zone is not None and self.time_zone.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-infra-clock-cfg:clock" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "summer-time"):
            if (self.summer_time is None):
                self.summer_time = Clock.SummerTime()
                self.summer_time.parent = self
                self._children_name_map["summer_time"] = "summer-time"
            return self.summer_time

        if (child_yang_name == "time-zone"):
            if (self.time_zone is None):
                self.time_zone = Clock.TimeZone()
                self.time_zone.parent = self
                self._children_name_map["time_zone"] = "time-zone"
            return self.time_zone

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "summer-time" or name == "time-zone"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Clock()
        return self._top_entity
