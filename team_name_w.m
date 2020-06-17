function [mat_name_w] = team_name_w(mat)
    % input  matrix of games with pairs of numbers
    Name_w = ["DEN", "MIN", "OKC", "POR", "UTA", "GSW", "LAC", "LAL", "PHX", "SAC", "DAL", "HOU", "MEM", "NOP", "SAS","portal_w"];
    [m,n] = size(mat);
    if n == 1
        for i=1:m
            team_name(i,1) = Name_w(mat(i,1));
        end
    else
        for i=1:m
            team_name(i,1) = Name_w(mat(i,1));
            team_name(i,2) = Name_w(mat(i,2));
        end
    end
    mat_name_w = team_name;
    end
    