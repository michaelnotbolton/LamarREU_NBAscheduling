function [mat_name_e] = team_name_e(mat)
    % input  matrix of games with pairs of numbers
    Name_e = ["BKN", "BOS", "NYK", "PHI", "TOR","CHI", "CLE", "DET", "IND", "MIL","ATL", "CHA", "MIA", "ORL", "WAS","portal_e"];
    [m,n] = size(mat);
    if n == 1
        for i=1:m
            team_name(i,1) = Name_e(mat(i,1));
        end
    else
        for i=1:m
            team_name(i,1) = Name_e(mat(i,1));
            team_name(i,2) = Name_e(mat(i,2));
        end
    end
    mat_name_e = team_name;
    end
    